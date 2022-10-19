import os
import typing

import var

from meta.SiteNodeMeta import SiteNodeMeta
from meta.parse.parse_site_node_meta import parse_site_node_meta
from info.DirectoryInfo import DirectoryInfo
from info.PostInfo import PostInfo
from info.parse.parse_directory_info import parse_directory_info
from tools.get_site_info import get_site_info
from tools.copy_statics import copy_statics
from render.render_directory import render_directory
from render.render_post import render_post
from render.render_post import render_site_root_post

################################################################################

render_directory_queue = []
render_post_queue = []
render_site_root_post_queue = []


def _one_directory(enter: SiteNodeMeta) -> typing.Tuple[DirectoryInfo, str]:
    dir_info = parse_directory_info(enter)

    output_path = os.path.relpath(enter.path, var.site_work_dir)
    output_path = os.path.join(var.output_work_dir, output_path, "index.html")

    return dir_info, output_path


def _one_post(post_info: PostInfo) -> typing.Tuple[PostInfo, str]:
    output_path = os.path.relpath(post_info.url, "/")
    output_path = os.path.join(var.output_work_dir, output_path)
    output_path = os.path.splitext(output_path)[0] + ".html"

    return post_info, output_path


def do_parse():
    site_tree = parse_site_node_meta(var.site_work_dir)

    enters = site_tree.child_node
    for enter in enters:
        dir_info, dir_output_path = _one_directory(enter)

        render_directory_queue.append((dir_info.__dict__, dir_output_path))

        for post in dir_info.posts:
            post_info, post_output_path = _one_post(post)
            render_post_queue.append((post_info.__dict__, post_output_path))
        enters.extend(enter.child_node)

    site_first_dir_info, _ = _one_directory(site_tree)
    for post in site_first_dir_info.posts:
        post_info, post_output_path = _one_post(post)
        render_site_root_post_queue.append((post_info.__dict__, post_output_path))


################################################################################


def do_render():
    site_info = get_site_info()

    copy_statics()

    for info, output_path in render_directory_queue:
        render_directory(site_info, info, output_path)

    for info, output_path in render_post_queue:
        render_post(site_info, info, output_path)

    for info, output_path in render_site_root_post_queue:
        render_site_root_post(site_info, info, output_path)
