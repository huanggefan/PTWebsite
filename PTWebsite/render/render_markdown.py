import typing

import markdown
import markdown.extensions.extra
import markdown.blockprocessors
import markdown.blockparser

import meta.PostMeta


# TODO 实现 "## 11" -> "<h2 id='11'>11</h2>"
class TitleIDRender(markdown.blockprocessors.BlockProcessor):
    def __init__(self, parser: markdown.blockparser.BlockParser):
        super().__init__(parser)

    def test(self, parent, block):
        pass

    def run(self, parent, blocks):
        pass


class TitleIDRenderExtension(markdown.Extension):
    def __init__(self, **kwargs: typing.Any):
        super().__init__(**kwargs)

    def extendMarkdown(self, md: markdown.Markdown):
        md.parser.blockprocessors.register(
            TitleIDRender(md.parser), 'TitleIDRender', 175
        )


def _render_markdown(md: str) -> str:
    markdown_render_extensions = (
        markdown.extensions.extra.ExtraExtension(),
        TitleIDRenderExtension(),
    )
    markdown_render = markdown.Markdown(extensions=markdown_render_extensions, output_format="html")

    return markdown_render.convert(md)


def render_markdown(post_meta: meta.PostMeta.PostMeta) -> str:
    return _render_markdown(post_meta.markdown)


if __name__ == "__main__":
    pass
