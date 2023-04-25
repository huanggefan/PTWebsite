import json


def write_meta_dict(site_meta_path: str, data: dict):
    meta_file_str = json.dumps(data, indent=4, ensure_ascii=False)
    with open(site_meta_path, "w", encoding="utf-8") as f:
        f.write(meta_file_str)
