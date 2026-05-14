# Echo

A Live2D AI VTuber built as a microservices monorepo.

## Services

| Service | Access | License |
|---------|--------|---------|
| tts | public | GPL 2.0 |
| stt | public | GPL 2.0 |
| llm | private | |
| avatar | private | |
| memory | private | |

> [!NOTE]
> The private submodules are not publicly accessible. This is intentional.

## Setup

```bash
git clone git@github.com:ramonasuncion/echo.git
cd echo
git submodule update --init services/tts services/stt
uv sync
```