import mistune

_parse = mistune.create_markdown(renderer=None, plugins=["strikethrough"])

_BLOCK = {"paragraph", "heading", "list_item", "block_quote"}


def _render(tokens):
    out = []
    for token in tokens:
        kind = token["type"]

        if kind in ("text", "codespan", "block_code"):
            out.append(token["raw"])
        elif kind == "softbreak":
            out.append(" ")
        elif kind == "linebreak":
            out.append("\n")
        elif kind == "image":
            out.append(token.get("attrs", {}).get("alt", ""))
        elif "children" in token:
            out.append(_render(token["children"]))
            if kind in _BLOCK:
                out.append("\n")

    return "".join(out)


def strip_markdown(text: str) -> str:
    if not text:
        return text
    return _render(_parse(text)).strip()
