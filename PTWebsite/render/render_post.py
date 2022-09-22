import os

import parse.parse_site
import parse.parse_template
import info.SiteInfo
import render.tools
import var


def render_post(site_info: info.SiteInfo):
    for post in var.render_post_queue:
        post_info, output_path = post
        template = parse.parse_template.parse_template(var.templates_work_dir, "post")
        d = {
            "site": site_info,
            "post": post_info
        }
        render.tools.write_one(template, d, output_path)

    for post in var.render_site_post_queue:
        post_info, output_path = post
        name = os.path.splitext(os.path.relpath(post_info["url"], "/"))[0]
        template = parse.parse_template.parse_template(var.templates_work_dir, name)
        d = {
            "site": site_info,
            "post": post_info
        }
        render.tools.write_one(template, d, output_path)
