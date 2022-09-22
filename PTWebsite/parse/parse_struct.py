import os

import meta.SiteStructNodeMeta


def parse_struct(now_dir: str, name="", father=None) -> meta.SiteStructNodeMeta.SiteStructNodeMeta:
    node = meta.SiteStructNodeMeta.SiteStructNodeMeta()

    dirs = []
    files = []

    for dir_entry in os.scandir(now_dir):
        assert isinstance(dir_entry, os.DirEntry)
        if dir_entry.is_dir():
            dirs.append(dir_entry)
        if dir_entry.is_file():
            files.append(dir_entry)

    node.father_node = father
    node.name = name

    if father is not None:
        node.path = os.path.join(father.path, name)
    else:
        node.path = now_dir

    for d in dirs:
        if d.name != "statics":
            n = parse_struct(d.path, d.name, node)
            node.child_node.append(n)
    node.child_node.sort(key=lambda x: x.name)

    for f in files:
        if os.path.splitext(f.name)[-1] == ".md":
            node.posts.append(f.path)
    node.posts.sort()

    return node
