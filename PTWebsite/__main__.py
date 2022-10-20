#!/bin/env python3

import argparse
import sys

import jinja2

import var
import do


def do_version(arg: argparse.Namespace):
    print("version:", var.__version__)
    print("    jinja2 version:", jinja2.__version__)


def _do_main_show():
    print("-------------------------------------------------------------------")
    print("root:", var.work_dir)
    print("site dir:", var.site_work_dir)
    print("meta file:", var.meta_work_dir)
    print("templates dir", var.templates_work_dir)
    print("output dir:", var.output_work_dir)
    print("-------------------------------------------------------------------")


def do_main(arg: argparse.Namespace):
    var.set_var(arg)

    if not var.quiet:
        _do_main_show()

    do.do_parse()
    do.do_render()
    do.do_copy()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='PTWebsite')

    parser.add_argument("-r", "--root", help="root dir", type=str)
    parser.add_argument("-v", "--version", help="show version information", action="store_true")
    parser.add_argument("--quiet", help="silent mode, no dot log anythings", action="store_true")

    if len(sys.argv) < 2:
        parser.print_help()
    else:
        args = parser.parse_args()
        if args.version:
            do_version(args)
        else:
            do_main(args)
