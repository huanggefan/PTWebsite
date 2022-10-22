#!/bin/env python3

import argparse
import sys

import jinja2

import var
import do


def _do_show_info():
    print("-------------------------------------------------------------------")
    print("root:", var.work_dir)
    print("site dir:", var.site_work_dir)
    print("meta file:", var.meta_work_dir)
    print("templates dir", var.templates_work_dir)
    print("output dir:", var.output_work_dir)
    print("-------------------------------------------------------------------")


def do_version():
    print("version:", var.__version__)
    print("    jinja2 version:", jinja2.__version__)


def do_serve():
    do.do_serve()


def do_main():
    do.do_copy()
    do.do_parse()
    do.do_render()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='PTWebsite')

    parser.add_argument("-r", "--root", help="root dir", type=str)
    parser.add_argument("-s", "--serve", help="start basic http server", action="store_true")
    parser.add_argument("-v", "--version", help="show version information", action="store_true")
    parser.add_argument("--quiet", help="silent mode, no dot log anythings", action="store_true")

    if len(sys.argv) < 2:
        parser.print_help()
        exit(0)

    args = parser.parse_args()
    var.set_var(args)

    if not var.quiet:
        _do_show_info()

    if args.version:
        do_version()
    elif args.serve:
        do_serve()
    else:
        do_main()
