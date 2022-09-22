import os
import typing

from parse.parse_struct import parse_struct
from parse.parse_directory_info import parse_directory_info
import info.PostInfo
import info.DirectoryInfo
import meta.SiteStructNodeMeta
import meta.SiteMeta
import render.render_directory
import render.render_post
import render.tools
import var


def _do_one_directory(enter: meta.SiteStructNodeMeta.SiteStructNodeMeta) -> typing.Tuple[info.DirectoryInfo.DirectoryInfo, str]:
    dir_info = parse_directory_info(enter)

    output_path = os.path.relpath(enter.path, var.site_work_dir)
    output_path = os.path.join(var.output_work_dir, output_path, "index.html")

    return dir_info, output_path


def _do_one_post(post_info: info.PostInfo.PostInfo) -> typing.Tuple[info.PostInfo.PostInfo, str]:
    output_path = os.path.relpath(post_info.url, "/")
    output_path = os.path.join(var.output_work_dir, output_path)
    output_path = os.path.splitext(output_path)[0] + ".html"

    return post_info, output_path


def do_parse():
    site_tree = parse_struct(var.site_work_dir)

    enters = site_tree.child_node
    for enter in enters:
        dir_info, dir_output_path = _do_one_directory(enter)
        var.render_directory_queue.append((dir_info.__dict__, dir_output_path))
        for post in dir_info.posts:
            post_info, post_output_path = _do_one_post(post)
            var.render_post_queue.append((post_info.__dict__, post_output_path))
        enters.extend(enter.child_node)

    site_first_dir_info, _ = _do_one_directory(site_tree)
    for post in site_first_dir_info.posts:
        post_info, post_output_path = _do_one_post(post)
        var.render_site_post_queue.append((post_info.__dict__, post_output_path))


def do_render():
    site_info = render.tools.get_site_info()
    render.tools.copy_statics()
    render.render_directory.render_directory(site_info)
    render.render_post.render_post(site_info)
