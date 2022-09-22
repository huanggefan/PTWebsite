import os
import typing

import info.PostInfo
import parse.parse_post
import parse.parse_site
import render.render_markdown
import var


def parse_post_info(post_md_path: str) -> typing.Optional[info.PostInfo.PostInfo]:
    result = info.PostInfo.PostInfo()
    post_meta = parse.parse_post.parse_post(post_md_path)

    result.url = os.path.relpath(post_md_path, var.site_work_dir)
    result.url = os.path.splitext(result.url)[0] + ".html"
    result.url = os.path.join("/", result.url)
    result.title = post_meta.title
    result.key_words = post_meta.key_words
    result.description = post_meta.description
    result.create_time = post_meta.create_time
    result.update_time = post_meta.update_time
    result.markdown = post_meta.markdown
    result.html = render.render_markdown.render_markdown(post_meta)

    return result
