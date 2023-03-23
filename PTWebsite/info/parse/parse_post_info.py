import os
import typing
import datetime

import var
from meta.parse.parse_post_meta import parse_post_meta
from info.PostInfo import PostInfo
from tools.markdown_to_html import markdown_to_html

now = datetime.datetime.now()


def parse_post_info(md_file_path: str) -> typing.Optional[PostInfo]:
    result = PostInfo()
    post_meta = parse_post_meta(md_file_path)

    result.url = os.path.relpath(post_meta.path, var.site_work_dir)
    result.url = os.path.splitext(result.url)[0] + ".html"
    result.url = os.path.join("/", result.url)

    result.title = post_meta.title
    result.key_words = post_meta.key_words
    result.description = post_meta.description

    if post_meta.thumbnail != "":
        result.thumbnail_url = post_meta.thumbnail
        result.thumbnail_alt = os.path.split(post_meta.thumbnail)[-1]

    result.create_time = post_meta.create_time
    result.update_time = post_meta.update_time
    result.release_time = post_meta.release_time

    result.template = post_meta.template

    result.json = post_meta.json

    result.markdown = post_meta.markdown
    result.html = markdown_to_html(post_meta)

    result.render_src = md_file_path
    result.render_dist = os.path.relpath(md_file_path, var.site_work_dir)
    result.render_dist = os.path.join(var.output_work_dir, result.render_dist)
    result.render_dist = os.path.splitext(result.render_dist)[0] + ".html"

    if result.release_time > now:
        return None
    else:
        return result


if __name__ == "__main__":
    var.site_work_dir = "../../../demo/site"
    var.output_work_dir = "../../../demo/output"
    post_info = parse_post_info("../../../demo/site/栏目2/栏目2-1文章1.md")
    print(post_info)
