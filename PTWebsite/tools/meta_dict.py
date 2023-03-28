import json


def write_meta_dict(site_meta_path: str, data: dict):
    meta_file_str = json.dumps(data, indent=4)
    with open(site_meta_path, "w") as f:
        f.write(meta_file_str)
