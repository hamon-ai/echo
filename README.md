# Echo

A Live2D AI VTuber built as a microservices monorepo.

## Services

| Service | Access | License |
|---------|--------|---------|
| [tts](https://github.com/ramonasuncion/echo-tts-service) | public | GPL 2.0 |
| [stt](https://github.com/ramonasuncion/echo-stt-service) | public | GPL 2.0 |
| [panel](https://github.com/ramonasuncion/echo-panel-service) | public | GPL 2.0 |
| [llm](https://github.com/ramonasuncion/echo-llm-service) | private | |
| [avatar](https://github.com/ramonasuncion/echo-avatar-service) | private | |
| [memory](https://github.com/ramonasuncion/echo-memory-service) | private | |

> [!NOTE]
> The private submodules are not publicly accessible. This is intentional.

## Setup

```bash
git clone git@github.com:IntelligentSandbox/echo.git
cd echo
git submodule update --init services/tts services/stt services/panel
uv sync
```