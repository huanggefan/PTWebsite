import json

import meta.SiteMeta


def _write_meta_dict(meta_path: str, data: dict):
    meta_file_str = json.dumps(data, indent=4)
    with open(meta_path, "w") as f:
        f.write(meta_file_str)


def _write_default_meta(meta_path: str):
    m = meta.SiteMeta.SiteMeta()
    meta_json = m.__dict__()
    _write_meta_dict(meta_path, meta_json)


def parse_site(meta_path: str) -> meta.SiteMeta.SiteMeta:
    m = meta.SiteMeta.SiteMeta()

    try:
        with open(meta_path, "r") as f:
            meta_file_str = f.read()
    except FileNotFoundError:
        _write_default_meta(meta_path)
        return m

    try:
        meta_json = json.loads(meta_file_str)
    except json.decoder.JSONDecodeError:
        _write_default_meta(meta_path)
        return m

    customer_meta = {}
    for k, v in meta_json.items():
        if k in list(m.__dict__().keys()):
            m.__setattr__(k, v)
        else:
            customer_meta[k] = v
    m.customer_meta = dict(m.customer_meta, **customer_meta)

    meta_json = m.__dict__()
    _write_meta_dict(meta_path, meta_json)

    return m
