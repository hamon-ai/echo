# Echo

A Live2D AI VTuber built as a microservices monorepo.

## Services

| Service                                      | Access  | License |
| -------------------------------------------- | ------- | ------- |
| [tts](https://github.com/ramonlabs/tts)       | public  | GPL 2.0 |
| [stt](https://github.com/ramonlabs/stt)       | public  | GPL 2.0 |
| [panel](https://github.com/ramonlabs/panel)   | public  | GPL 2.0 |
| [llm](https://github.com/ramonlabs/llm)       | private |         |
| [avatar](https://github.com/ramonlabs/avatar) | private |         |
| [memory](https://github.com/ramonlabs/memory) | private |         |

> [!NOTE]
> The private submodules are not publicly accessible. This is intentional.

## Setup

```bash
git clone git@github.com:ramonlabs/echo.git
cd echo
git submodule update --init services/tts services/stt services/panel
uv sync
```