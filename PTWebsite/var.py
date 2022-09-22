import os
import argparse

work_dir = ""
site_work_dir = ""
meta_work_dir = ""
templates_work_dir = ""
output_work_dir = ""

quiet = False

render_directory_queue = []
render_post_queue = []
render_site_post_queue = []

__version__ = "0.0.1"


def set_var(arg: argparse.Namespace):
    global work_dir
    global site_work_dir
    global meta_work_dir
    global templates_work_dir
    global output_work_dir
    global quiet

    work_dir = arg.root
    site_work_dir = os.path.join(work_dir, "site")
    meta_work_dir = os.path.join(work_dir, "meta.json")
    templates_work_dir = os.path.join(work_dir, "templates")
    output_work_dir = os.path.join(work_dir, "output")
    quiet = arg.quiet
