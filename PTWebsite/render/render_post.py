import os

import var
from info.SiteInfo import SiteInfo
from tools.load_template import load_template
from tools.render_one import render_one


def render_post(site_info: SiteInfo, post_info: dict, output_path: str):
    template = load_template(var.templates_work_dir, "post")

    d = {
        "site": site_info,
        "post": post_info
    }

    render_one(template, d, output_path)


def render_site_root_post(site_info: SiteInfo, post_info: dict, output_path: str):
    name = os.path.splitext(os.path.relpath(post_info.get("url"), "/"))[0]

    template = load_template(var.templates_work_dir, name)

    d = {
        "site": site_info,
        "post": post_info
    }

    render_one(template, d, output_path)
