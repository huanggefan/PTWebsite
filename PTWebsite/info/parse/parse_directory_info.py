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


def _get_all_posts(node: SiteNodeMeta) -> list[PostInfo]:
    r = []

    r.extend(
        _get_posts(node)
    )

    for child_node in node.child_node:
        r.extend(
            _get_all_posts(child_node)
        )

    return r


def _parse_directory_info_one(node: SiteNodeMeta) -> DirectoryInfo:
    result = DirectoryInfo()
    result.url = os.path.join("/", os.path.relpath(node.path, var.site_work_dir), "index.html")
    result.name = node.name

    return result


def parse_directory_info(node: SiteNodeMeta) -> DirectoryInfo:
    result = DirectoryInfo()

    result.url = os.path.join("/", os.path.relpath(node.path, var.site_work_dir), "index.html")
    result.name = node.name
    result.posts = _get_posts(node)
    result.all_posts = _get_all_posts(node)

    result.posts.sort(key=lambda x: x.release_time, reverse=True)
    result.all_posts.sort(key=lambda x: x.release_time, reverse=True)

    return result


if __name__ == "__main__":
    from meta.parse.parse_site_node_meta import parse_site_node_meta
    site_node_meta = parse_site_node_meta("../../../demo/site/栏目1", "", None)
    directory_info = parse_directory_info(site_node_meta)
    print(directory_info)
