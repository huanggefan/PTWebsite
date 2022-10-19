import os

import meta.SiteNodeMeta


def parse_site_node_meta(now_dir: str, now_name="", father_node=None) -> meta.SiteNodeMeta.SiteNodeMeta:
    node = meta.SiteNodeMeta.SiteNodeMeta()

    dirs = []
    files = []

    for dir_entry in os.scandir(now_dir):
        assert isinstance(dir_entry, os.DirEntry)
        if dir_entry.is_dir():
            dirs.append(dir_entry)
        if dir_entry.is_file():
            files.append(dir_entry)

    node.father_node = father_node
    node.name = now_name

    if father_node is not None:
        node.path = os.path.join(father_node.path, now_name)
    else:
        node.path = now_dir

    for d in dirs:
        if d.name != "statics":
            n = parse_site_node_meta(d.path, d.name, node)
            node.child_node.append(n)
    node.child_node.sort(key=lambda x: x.name)

    for f in files:
        if os.path.splitext(f.name)[-1] == ".md":
            node.post_files.append(f.path)
    node.post_files.sort()

    return node


if __name__ == "__main__":
    site_node_tree = parse_site_node_meta("../../../demo/site", "", None)
    site_node_tree.print()
