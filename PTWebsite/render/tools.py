import os
import shutil

import jinja2

import info.SiteInfo
import parse.parse_site
import var


def copy_statics():
    os.makedirs(var.output_work_dir, exist_ok=True)
    shutil.copytree(os.path.join(var.site_work_dir, "statics"), os.path.join(var.output_work_dir, "statics"), dirs_exist_ok=True)

    for entry in os.scandir(var.templates_work_dir):
        assert isinstance(entry, os.DirEntry)
        if not entry.is_file() and not entry.is_dir():
            continue
        if entry.is_file():
            shutil.copyfile(entry.path, os.path.join(var.output_work_dir, entry.name))
        elif entry.is_dir():
            shutil.copytree(entry.path, os.path.join(var.output_work_dir, entry.name), dirs_exist_ok=True)

        if not var.quiet:
            print("copy:", os.path.join(var.output_work_dir, entry.name))


def write_one(template: jinja2.Template, info: dict, output_path: str):
    if template is None:
        return
    result = template.render(info)
    os.makedirs(os.path.split(output_path)[0], exist_ok=True)
    with open(output_path, "w") as f:
        f.write(result)

    if not var.quiet:
        print("render:", output_path)


def get_site_info() -> info.SiteInfo:
    site_meta = parse.parse_site.parse_site(var.meta_work_dir)
    site_info = info.SiteInfo.SiteInfo()
    site_info.name = site_meta.name
    site_info.owner = site_meta.owner
    site_info.key_words = site_meta.key_words
    site_info.description = site_meta.description
    site_info.customer_meta = site_meta.customer_meta

    return site_info
