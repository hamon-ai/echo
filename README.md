# Echo

A Live2D AI VTuber built as a microservices monorepo.

## Services

| Service                                      | Access  | License |
| -------------------------------------------- | ------- | ------- |
| [tts](https://github.com/hamon-ai/tts)       | public  | GPL 2.0 |
| [stt](https://github.com/hamon-ai/stt)       | public  | GPL 2.0 |
| [panel](https://github.com/hamon-ai/panel)   | public  | GPL 2.0 |
| [llm](https://github.com/hamon-ai/llm)       | private |         |
| [avatar](https://github.com/hamon-ai/avatar) | private |         |
| [memory](https://github.com/hamon-ai/memory) | private |         |

> [!NOTE]
> The private submodules are not publicly accessible. This is intentional.

## Setup

```bash
git clone git@github.com:hamon-ai/echo.git
cd echo
git submodule update --init services/tts services/stt services/panel
uv sync
```