from contextlib import asynccontextmanager
from typing import AsyncIterator

import httpx


class ServiceError(Exception):
    """Base domain error carrying a stable code and a human-readable message."""

    code: str = "internal_error"
    message: str = "Something went wrong."
    http_status: int = 500

    def __init__(self, message: str | None = None):
        if message:
            self.message = message
        super().__init__(self.message)


class TtsAuthError(ServiceError):
    code = "tts_auth"
    http_status = 502
    message = "TTS auth failed, check tts.api_key in private/config.yaml"


class TtsUnavailable(ServiceError):
    code = "tts_unavailable"
    http_status = 502
    message = "Voice service is unavailable."


class LlmError(ServiceError):
    code = "llm_error"
    http_status = 502
    message = "Language model request failed."


class LlmRateLimited(LlmError):
    code = "llm_rate_limited"
    http_status = 429
    message = "Rate limited. Wait a minute or switch to Ollama."


class SttError(ServiceError):
    code = "stt_error"
    http_status = 502
    message = "Speech-to-text failed."


# named to avoid shadowing the builtin MemoryError
class MemoryServiceError(ServiceError):
    code = "memory_error"
    http_status = 502
    message = "Memory service failed."


def to_payload(exc: ServiceError) -> dict[str, str]:
    """Shape a domain error into the wire vocabulary clients consume."""
    return {"code": exc.code, "message": exc.message}


def as_service_error(exc: Exception) -> ServiceError:
    """Pass through domain errors, wrap anything unexpected as generic."""
    return exc if isinstance(exc, ServiceError) else ServiceError()


# each service gets its own error types used when mapping an upstream failure
_AUTH: dict[str, type[ServiceError]] = {"tts": TtsAuthError}
_UNAVAILABLE: dict[str, type[ServiceError]] = {
    "tts": TtsUnavailable,
    "llm": LlmError,
    "stt": SttError,
    "memory": MemoryServiceError,
}


def from_upstream(service: str, exc: Exception) -> ServiceError:
    """Map an upstream httpx failure to the right domain error."""
    unavailable = _UNAVAILABLE.get(service, ServiceError)

    if isinstance(exc, httpx.HTTPStatusError):
        status = exc.response.status_code
        if status == 401:
            return _AUTH.get(service, unavailable)()
        if status == 429:
            return LlmRateLimited()
        if status >= 500:
            return unavailable()
        return unavailable()

    # timeouts, connection refused and other transport errors
    return unavailable()


@asynccontextmanager
async def upstream(service: str) -> AsyncIterator[None]:
    """Wrap an httpx call block, converting transport errors to domain errors."""
    try:
        yield
    except ServiceError:
        raise
    except (httpx.HTTPStatusError, httpx.TimeoutException, httpx.RequestError) as e:
        raise from_upstream(service, e) from e
