import var

from info.SiteInfo import SiteInfo
from tools.load_template import load_template
from tools.render_one import render_one


def render_directory(site_info: SiteInfo, directory_info: dict, output_path: str):
    template = load_template(var.templates_work_dir, "directory")

    d = {
        "site":      site_info,
        "directory": directory_info
    }

    render_one(template, d, output_path)
