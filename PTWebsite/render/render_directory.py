import parse.parse_site
import parse.parse_template
import info.SiteInfo
import render.tools
import var


def render_directory(site_info: info.SiteInfo):
    for directory in var.render_directory_queue:
        directory_info, output_path = directory
        template = parse.parse_template.parse_template(var.templates_work_dir, "directory")
        d = {
            "site":      site_info,
            "directory": directory_info
        }
        render.tools.write_one(template, d, output_path)
