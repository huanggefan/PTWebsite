import os

import var
from meta.parse.parse_site_node_meta import parse_site_node_meta
from meta.SiteNodeMeta import SiteNodeMeta
from info.parse.parse_directory_info import parse_directory_info
from info.DirectoryInfo import DirectoryInfo
from tools.get_site_info import get_site_info
from tools.copy_statics import copy_templates_statics
from tools.copy_statics import copy_site_statics
from render.render_directory import render_directory
from render.render_post import render_post
from render.render_post import render_site_root_post

################################################################################


render_directory_queue = []
render_post_queue = []
render_root_post_queue = []

site_node_meta_tree = SiteNodeMeta()
directory_info_tree = DirectoryInfo()


################################################################################


def do_parse():
    global site_node_meta_tree
    global directory_info_tree

    site_node_meta_tree = parse_site_node_meta(var.site_work_dir)
    directory_info_tree = parse_directory_info(site_node_meta_tree)

    directory_enters = directory_info_tree.child_node
    for directory_info_node in directory_enters:
        render_directory_queue.append(directory_info_node)
        directory_enters.extend(directory_info_node.child_node)

    render_post_queue.extend(directory_info_tree.all_posts)
    render_root_post_queue.extend(directory_info_tree.posts)


################################################################################


def do_render():
    site_info = get_site_info()

    for info in render_directory_queue:
        render_directory(site_info, info)

    for info in render_post_queue:
        render_post(site_info, info)

    for info in render_root_post_queue:
        render_site_root_post(site_info, info, directory_info_tree)


################################################################################


def do_copy():
    os.makedirs(var.output_work_dir, exist_ok=True)

    copy_templates_statics()
    copy_site_statics()
