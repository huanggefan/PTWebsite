import os

import var

from meta.SiteNodeMeta import SiteNodeMeta
from info.SiteInfo import SiteInfo
from info.PostInfo import PostInfo
from info.DirectoryInfo import DirectoryInfo
from info.parse.parse_post_info import parse_post_info


def __get_posts(node: SiteNodeMeta) -> list[PostInfo]:
    r = []
    for p in node.post_files:
        post_info = parse_post_info(p)
        if post_info is not None:
            r.append(post_info)
    return r


def __parse_directory_info_all_posts(node_tree_now: DirectoryInfo):
    for nc in node_tree_now.child_node:
        __parse_directory_info_all_posts(nc)

    for nc in node_tree_now.child_node:
        node_tree_now.all_posts.extend(nc.all_posts)

    if node_tree_now.father_node is not None:
        node_tree_now.all_posts.extend(node_tree_now.posts)

    node_tree_now.all_posts.sort(key=lambda x: x.release_time, reverse=True)


def __parse_directory_info(site_info: SiteInfo, node: SiteNodeMeta, father: DirectoryInfo = None) -> DirectoryInfo:
    info_node = DirectoryInfo()

    info_node.name = node.name

    if father is None:
        info_node.url = "/index.html"
    else:
        info_node.url = os.path.relpath(node.path, var.site_work_dir)
        info_node.url = os.path.join("/", info_node.url, "index.html")

    if father is None:
        info_node.key_words = site_info.key_words
        info_node.description = site_info.description
        info_node.customer_meta = site_info.customer_meta
    else:
        info_node.key_words = node.key_words
        info_node.description = node.description
        info_node.template = node.template
        info_node.customer_meta = node.customer_meta

    if node.thumbnail != "":
        info_node.thumbnail_url = node.thumbnail
        info_node.thumbnail_alt = os.path.split(node.thumbnail)[-1]

    info_node.posts = __get_posts(node)
    info_node.posts.sort(key=lambda x: x.release_time, reverse=True)

    info_node.father_node = father

    for child in node.child_node:
        info_node.child_node.append(
            __parse_directory_info(site_info, child, info_node)
        )

    info_node.render_src = node.path
    info_node.render_dist = os.path.relpath(info_node.render_src, var.site_work_dir)
    info_node.render_dist = os.path.join(var.output_work_dir, info_node.render_dist, "index.html")

    return info_node


def parse_directory_info(site_info: SiteInfo, node: SiteNodeMeta) -> DirectoryInfo:
    directory_info_tree = __parse_directory_info(site_info, node, None)
    __parse_directory_info_all_posts(directory_info_tree)

    return directory_info_tree


if __name__ == "__main__":
    from meta.parse.parse_site_node_meta import parse_site_node_meta
    from meta.parse.parse_site_meta import parse_site_meta
    from info.parse.parse_site_info import parse_site_info

    var.site_work_dir = "../../../demo/site"
    var.output_work_dir = "../../../demo/output"

    site_meta = parse_site_meta("../../../demo/meta.json")
    site_info = parse_site_info(site_meta)
    site_node_meta = parse_site_node_meta("../../../demo/site")
    info_tree = parse_directory_info(site_info, site_node_meta)
    print(info_tree)
