import os

import var
from meta.SiteNodeMeta import SiteNodeMeta
from info.PostInfo import PostInfo
from info.DirectoryInfo import DirectoryInfo
from info.parse.parse_post_info import parse_post_info


def _get_posts(node: SiteNodeMeta) -> list[PostInfo]:
    r = []
    for p in node.post_files:
        post_info = parse_post_info(p)
        if post_info is not None:
            r.append(post_info)
    return r


def _parse_directory_info_all_posts(node_tree_now: DirectoryInfo):
    for nc in node_tree_now.child_node:
        _parse_directory_info_all_posts(nc)

    for nc in node_tree_now.child_node:
        node_tree_now.all_posts.extend(nc.all_posts)

    if node_tree_now.father_node is not None:
        node_tree_now.all_posts.extend(node_tree_now.posts)

    node_tree_now.all_posts.sort(key=lambda x: x.release_time, reverse=True)


def _parse_directory_info(node: SiteNodeMeta, father: DirectoryInfo = None) -> DirectoryInfo:
    info_node = DirectoryInfo()

    if father is None:
        info_node.url = "/index.html"
    else:
        info_node.url = os.path.relpath(node.path, var.site_work_dir)
        info_node.url = os.path.join("/", info_node.url, "index.html")

    info_node.name = node.name
    info_node.father_node = father

    info_node.render_src = node.path
    info_node.render_dist = os.path.relpath(info_node.render_src, var.site_work_dir)
    info_node.render_dist = os.path.join(var.output_work_dir, info_node.render_dist, "index.html")

    info_node.posts = _get_posts(node)
    info_node.posts.sort(key=lambda x: x.release_time, reverse=True)

    for c in node.child_node:
        info_node.child_node.append(
            _parse_directory_info(c, info_node)
        )

    return info_node


def parse_directory_info(node: SiteNodeMeta) -> DirectoryInfo:
    directory_info_tree = _parse_directory_info(node, None)
    _parse_directory_info_all_posts(directory_info_tree)

    return directory_info_tree


if __name__ == "__main__":
    from meta.parse.parse_site_node_meta import parse_site_node_meta

    var.site_work_dir = "../../../demo/site"
    var.output_work_dir = "../../../demo/output"

    site_node_meta = parse_site_node_meta("../../../demo/site")
    info_tree = parse_directory_info(site_node_meta)
    print(info_tree)
