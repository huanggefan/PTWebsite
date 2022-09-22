import os

import info.DirectoryInfo
import info.PostInfo
import meta.SiteStructNodeMeta
import parse.parse_site
import parse.parse_post_info
import var


def _get_posts(node: meta.SiteStructNodeMeta.SiteStructNodeMeta) -> list[info.PostInfo.PostInfo]:
    r = []
    for p in node.posts:
        post_info = parse.parse_post_info.parse_post_info(p)
        if post_info is not None:
            r.append(post_info)
    return r


def _get_all_posts(node: meta.SiteStructNodeMeta.SiteStructNodeMeta) -> list[info.PostInfo.PostInfo]:
    r = []

    r.extend(
        _get_posts(node)
    )

    for child_node in node.child_node:
        r.extend(
            _get_all_posts(child_node)
        )

    return r


def _parse_directory_info_one(node: meta.SiteStructNodeMeta.SiteStructNodeMeta) -> info.DirectoryInfo.DirectoryInfo:
    result = info.DirectoryInfo.DirectoryInfo()
    result.url = os.path.join("/", os.path.relpath(node.path, var.site_work_dir), "index.html")
    result.name = node.name

    return result


def parse_directory_info(node: meta.SiteStructNodeMeta.SiteStructNodeMeta) -> info.DirectoryInfo.DirectoryInfo:
    result = info.DirectoryInfo.DirectoryInfo()

    info.url = os.path.join("/", os.path.relpath(node.path, var.site_work_dir), "index.html")
    result.name = node.name
    result.posts = _get_posts(node)
    result.all_posts = _get_all_posts(node)

    return result
