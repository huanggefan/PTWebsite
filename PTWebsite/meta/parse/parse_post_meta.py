import re
import datetime
import typing
import os.path

import meta.PostMeta

match_title_re = r'''@Title (.*?)@'''
match_key_words_re = r'''@KeyWords (.*?)@'''
match_description_re = r'''@Description (.*?)@'''
match_create_time_re = r'''@CreateTime (.*?)@'''
match_update_time_re = r'''@UpdateTime (.*?)@'''
match_release_time_re = r'''@ReleaseTime (.*?)@'''

cover_file_ext = [".png", ".jpg", ".jpeg"]


def _parse_list_from_str(list_str: str) -> typing.List[str]:
    list_str = list_str.replace(" ", "")
    return list_str.split(",")


def _parse_datetime_form_str(datetime_str: str) -> typing.Optional[datetime.datetime]:
    try:
        return datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return datetime.datetime.strptime(datetime_str, "%Y-%m-%d")
    except Exception:
        return None


scan_markdown_lines_limit = 12


def _get_title_from_md(md_lines: list) -> str:
    for i in range(scan_markdown_lines_limit):
        if i >= len(md_lines):
            return ""
        md = md_lines[i]
        match_result = re.match(match_title_re, md)
        if match_result is not None:
            return match_result.groups()[0]
        else:
            return ""


def _get_key_words_from_md(md_lines: list) -> typing.List[str]:
    for i in range(scan_markdown_lines_limit):
        if i >= len(md_lines):
            return []
        md = md_lines[i]
        match_result = re.match(match_key_words_re, md)
        if match_result is not None:
            return _parse_list_from_str(match_result.groups()[0])
        else:
            return []


def _get_description_from_md(md_lines: list) -> str:
    for i in range(scan_markdown_lines_limit):
        if i >= len(md_lines):
            return ""
        md = md_lines[i]
        match_result = re.match(match_description_re, md)
        if match_result is not None:
            return match_result.groups()[0]
        else:
            return ""


def _get_create_time_from_md(md_lines: list) -> typing.Optional[datetime.datetime]:
    for i in range(scan_markdown_lines_limit):
        if i >= len(md_lines):
            return None
        md = md_lines[i]
        match_result = re.match(match_create_time_re, md)
        if match_result is not None:
            return _parse_datetime_form_str(match_result.groups()[0])


def _get_update_time_from_md(md_lines: list) -> typing.Optional[datetime.datetime]:
    for i in range(scan_markdown_lines_limit):
        if i >= len(md_lines):
            return None
        md = md_lines[i]
        match_result = re.match(match_update_time_re, md)
        if match_result is not None:
            return _parse_datetime_form_str(match_result.groups()[0])


def _get_release_time_from_md(md_lines: list) -> typing.Optional[datetime.datetime]:
    for i in range(scan_markdown_lines_limit):
        if i >= len(md_lines):
            return None
        md = md_lines[i]
        match_result = re.match(match_release_time_re, md)
        if match_result is not None:
            return _parse_datetime_form_str(match_result.groups()[0])


def _get_title_from_file(md_file_path: str) -> str:
    filename = os.path.split(md_file_path)[-1]
    return os.path.splitext(filename)[0]


def _get_create_time_from_file(md_file_path: str) -> datetime.datetime:
    ct = os.path.getctime(md_file_path)
    return datetime.datetime.fromtimestamp(ct)


def _get_update_time_from_file(md_file_path: str) -> datetime.datetime:
    mt = os.path.getmtime(md_file_path)
    return datetime.datetime.fromtimestamp(mt)


def _get_markdown(md_file_text: str) -> str:
    md_lines = md_file_text.splitlines()
    new_md_lines = []

    for i in range(len(md_lines)):
        md = md_lines[i]
        if re.match(match_title_re, md) is not None:
            continue
        elif re.match(match_key_words_re, md) is not None:
            continue
        elif re.match(match_description_re, md) is not None:
            continue
        elif re.match(match_create_time_re, md) is not None:
            continue
        elif re.match(match_update_time_re, md) is not None:
            continue
        elif re.match(match_release_time_re, md) is not None:
            continue
        else:
            new_md_lines.append(md)

    return "\n".join(new_md_lines)


def _get_cover_file(md_file_path: str) -> str:
    file_dir, file_full_name = os.path.split(md_file_path)
    file_name, file_ext = os.path.splitext(file_full_name)

    for ext in cover_file_ext:
        name = file_name + ext
        cover_file_path = os.path.join(file_dir, name)

        if os.access(cover_file_path, os.R_OK):
            return cover_file_path

    return ""


def _get_meta(md_file_text: str, md_file_path: str) -> meta.PostMeta.PostMeta:
    post_meta = meta.PostMeta.PostMeta()

    md_lines = md_file_text.splitlines()

    post_meta.path = md_file_path
    post_meta.title = _get_title_from_md(md_lines)
    post_meta.key_words = _get_key_words_from_md(md_lines)
    post_meta.description = _get_description_from_md(md_lines)
    post_meta.cover_path = _get_cover_file(md_file_path)
    post_meta.create_time = _get_create_time_from_md(md_lines)
    post_meta.update_time = _get_update_time_from_md(md_lines)
    post_meta.release_time = _get_release_time_from_md(md_lines)

    if post_meta.title == "":
        post_meta.title = _get_title_from_file(md_file_path)
    if post_meta.create_time is None:
        post_meta.create_time = _get_create_time_from_file(md_file_path)
    if post_meta.update_time is None:
        post_meta.update_time = _get_update_time_from_file(md_file_path)
    if post_meta.release_time is None:
        post_meta.release_time = post_meta.create_time

    post_meta.markdown = _get_markdown(md_file_text)

    return post_meta


def parse_post_meta(md_path: str) -> meta.PostMeta.PostMeta:
    with open(md_path, "r") as f:
        md = f.read()
    return _get_meta(md, md_path)


if __name__ == "__main__":
    post_meta = parse_post_meta("../../../demo/site/栏目2/栏目2-1文章1.md")
    print(post_meta)
