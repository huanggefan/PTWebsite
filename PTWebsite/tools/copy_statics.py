import os
import shutil

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
