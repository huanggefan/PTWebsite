import json
import os

import meta.SiteNodeMeta
import tools.meta_dict


def __write_default_meta(meta_path: str) -> None:
    m = meta.SiteNodeMeta.SiteNodeMeta()
    meta_json = m.dict()
    tools.meta_dict.write_meta_dict(meta_path, meta_json)


def __gen_customer_meta(meta_json: dict, node: meta.SiteNodeMeta.SiteNodeMeta) -> None:
    customer_meta = {}
    for k, v in meta_json.items():
        if k in list(node.dict().keys()):
            node.__setattr__(k, v)
        else:
            customer_meta[k] = v
    node.customer_meta = dict(node.customer_meta, **customer_meta)


def __parse_site_node_meta_json(node: meta.SiteNodeMeta.SiteNodeMeta) -> None:
    meta_json_path = os.path.join(node.path, "meta.json")

    try:
        with open(meta_json_path, "r", encoding="utf-8") as f:
            meta_file_str = f.read()
    except FileNotFoundError:
        __write_default_meta(meta_json_path)
        return

    try:
        meta_json = json.loads(meta_file_str)
    except json.decoder.JSONDecodeError:
        __write_default_meta(meta_json_path)
        return

    __gen_customer_meta(meta_json, node)

    meta_json = node.dict()
    tools.meta_dict.write_meta_dict(meta_json_path, meta_json)


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

    node.name = now_name

    if father_node is not None:
        node.path = os.path.join(father_node.path, now_name)
    else:
        node.path = now_dir

    if father_node is not None:
        __parse_site_node_meta_json(node)

    for f in files:
        if os.path.splitext(f.name)[-1] == ".md":
            node.post_files.append(f.path)

    node.father_node = father_node

    for d in dirs:
        if d.name != "statics":
            n = parse_site_node_meta(d.path, d.name, node)
            node.child_node.append(n)
    node.child_node.sort(key=lambda x: x.name)

    return node


if __name__ == "__main__":
    site_node_tree = parse_site_node_meta("../../../demo/site", "", None)
    print(site_node_tree)
