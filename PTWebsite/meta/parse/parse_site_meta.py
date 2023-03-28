import json

import meta.SiteMeta
import tools.meta_dict


def __write_default_meta(site_meta_path: str) -> None:
    m = meta.SiteMeta.SiteMeta()
    meta_json = m.dict()
    tools.meta_dict.write_meta_dict(site_meta_path, meta_json)


def __gen_customer_meta(meta_json: dict, m: meta.SiteMeta.SiteMeta) -> None:
    customer_meta = {}
    for k, v in meta_json.items():
        if k in list(m.dict().keys()):
            m.__setattr__(k, v)
        else:
            customer_meta[k] = v
    m.customer_meta = dict(m.customer_meta, **customer_meta)


def parse_site_meta(site_meta_path: str) -> meta.SiteMeta.SiteMeta:
    m = meta.SiteMeta.SiteMeta()

    try:
        with open(site_meta_path, "r") as f:
            meta_file_str = f.read()
    except FileNotFoundError:
        __write_default_meta(site_meta_path)
        return m

    try:
        meta_json = json.loads(meta_file_str)
    except json.decoder.JSONDecodeError:
        __write_default_meta(site_meta_path)
        return m

    __gen_customer_meta(meta_json, m)

    meta_json = m.dict()
    tools.meta_dict.write_meta_dict(site_meta_path, meta_json)

    return m


if __name__ == "__main__":
    site_meta = parse_site_meta("../../../demo/meta.json")
    print(site_meta)
