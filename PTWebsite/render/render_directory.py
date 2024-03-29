import var

from info.SiteInfo import SiteInfo
from info.DirectoryInfo import DirectoryInfo
from tools.load_template import load_template
from tools.render_one import render_one


def render_directory(site_info: SiteInfo, directory_info: DirectoryInfo):
    template = None

    if directory_info.template != "":
        template_name = "customer/{}".format(directory_info.template)
        template = load_template(var.templates_work_dir, template_name)

    if template is None:
        template = load_template(var.templates_work_dir, "directory")

    d = {
        "site":      site_info,
        "directory": directory_info
    }

    render_one(template, d, directory_info.render_dist)
