import os
import jinja2

import var


def render_one(template: jinja2.Template, info: dict, output_path: str):
    if template is None:
        return

    result = template.render(info)

    os.makedirs(os.path.split(output_path)[0], exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    if not var.quiet:
        print("render:", output_path)
