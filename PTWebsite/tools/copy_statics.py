import os
import shutil

import var


def copy_templates_statics():
    for entry in os.scandir(var.templates_work_dir):
        assert isinstance(entry, os.DirEntry)

        s_src = entry.path
        s_dist = os.path.join(var.output_work_dir, entry.name)
        s_dist_dir = os.path.split(s_dist)[0]

        if not entry.is_file() and not entry.is_dir():
            continue
        else:
            os.makedirs(s_dist_dir, exist_ok=True)

        if entry.is_file():
            shutil.copyfile(s_src, s_dist)
        elif entry.is_dir():
            shutil.copytree(s_src, s_dist, dirs_exist_ok=True)

        if not var.quiet:
            print("copy:", s_dist)


def _copy_site_statics(now_dir: str):
    dirs = []
    files = []
    s = []

    for dir_entry in os.scandir(now_dir):
        assert isinstance(dir_entry, os.DirEntry)
        if dir_entry.is_dir():
            dirs.append(dir_entry)
        if dir_entry.is_file():
            files.append(dir_entry)

    for d in dirs:
        if d.name != "statics":
            s.extend(_copy_site_statics(d.path))

    for f in files:
        if os.path.splitext(f.name)[-1] != ".md":
            p = os.path.relpath(f.path, var.site_work_dir)
            p = os.path.join(var.output_work_dir, p)
            p = (f.path, p)
            s.append(p)

    return s


def copy_site_statics():
    statics = _copy_site_statics(var.site_work_dir)

    for s_src, s_dist in statics:
        s_dist_dir = os.path.split(s_dist)[0]

        os.makedirs(s_dist_dir, exist_ok=True)
        shutil.copyfile(s_src, s_dist)

        if not var.quiet:
            print("copy:", s_dist)


if __name__ == "__main__":
    var.output_work_dir = "../../demo/output"
    var.site_work_dir = "../../demo/site"
    copy_site_statics()
