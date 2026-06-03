# Echo

A Live2D AI VTuber built as a microservices monorepo.

## Services

| Service                                      | Access  | License |
| -------------------------------------------- | ------- | ------- |
| [tts](https://github.com/ramonics/tts)       | public  | GPL 2.0 |
| [stt](https://github.com/ramonics/stt)       | public  | GPL 2.0 |
| [panel](https://github.com/ramonics/panel)   | public  | GPL 2.0 |
| [llm](https://github.com/ramonics/llm)       | private |         |
| [avatar](https://github.com/ramonics/avatar) | private |         |
| [memory](https://github.com/ramonics/memory) | private |         |

> [!NOTE]
> The private submodules are not publicly accessible. This is intentional.

## Setup

```bash
git clone git@github.com:ramonics/echo.git
cd echo
git submodule update --init services/tts services/stt services/panel
uv sync
```