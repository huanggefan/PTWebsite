import os
import typing

import jinja2

_templates_dict = {
    "index":     None,
    "about":     None,
    "404":       None,
    "post":      None,
    "directory": None,
}


def _load_template(template_path: str) -> jinja2.Template:
    with open(template_path, "r") as f:
        t = f.read()

    return jinja2.Template(t)


def parse_template(work_dir: str, template_name: str) -> typing.Optional[jinja2.Template]:
    t = _templates_dict.get(template_name)
    if t is not None:
        return t

    template_path = os.path.join(work_dir, template_name) + ".html"
    if not os.path.exists(template_path):
        return None

    t = _load_template(template_path)
    _templates_dict[template_name] = t
    return t
