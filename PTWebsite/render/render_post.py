import os

import var
from info.SiteInfo import SiteInfo
from info.PostInfo import PostInfo
from info.DirectoryInfo import DirectoryInfo
from tools.load_template import load_template
from tools.render_one import render_one


def render_post(site_info: SiteInfo, post_info: PostInfo):
    template = None
    if post_info.template != "":
        template_name = "customer/{}".format(post_info.template)
        template = load_template(var.templates_work_dir, template_name)
    if template is None:
        template = load_template(var.templates_work_dir, "post")

    d = {
        "site": site_info,
        "post": post_info
    }

    render_one(template, d, post_info.render_dist)


def render_site_root_post(site_info: SiteInfo, post_info: PostInfo, directory_info_tree: DirectoryInfo):
    name = os.path.splitext(os.path.relpath(post_info.url, "/"))[0]

    template = load_template(var.templates_work_dir, name)

    d = {
        "site": site_info,
        "root": directory_info_tree,
        "post": post_info,
    }

    render_one(template, d, post_info.render_dist)
