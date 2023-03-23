import datetime
import json
import typing
import os.path

import meta.PostMeta


def _list_from_str(list_str: str) -> typing.List[str]:
    list_str = list_str.replace(" ", "")
    return list_str.split(",")


def _datetime_form_str(datetime_str: str) -> typing.Optional[datetime.datetime]:
    try:
        return datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


def _json_from_str(json_str) -> object:
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return {}


def _get_title_from_file(md_file_path: str) -> str:
    filename = os.path.split(md_file_path)[-1]
    return os.path.splitext(filename)[0]


def _get_create_time_from_file(md_file_path: str) -> datetime.datetime:
    ct = os.path.getctime(md_file_path)
    return datetime.datetime.fromtimestamp(ct)


def _get_update_time_from_file(md_file_path: str) -> datetime.datetime:
    mt = os.path.getmtime(md_file_path)
    return datetime.datetime.fromtimestamp(mt)


class ParsePostMetaDFA(object):
    def __init__(self):
        self.length = 0
        self.text = ""

        self.pointer = 0
        self.key_buffer = ""
        self.value_buffer = ""
        self.markdown_buffer = ""

        self.func = self.__f_start

        self.result = {}

    def do(self, md_path: str) -> meta.PostMeta.PostMeta | None:
        with open(md_path, "r") as f:
            self.text = f.read()
            self.length = len(self.text)

        while self.pointer < self.length and self.func != self.__f_finish:
            self.func()

        post_meta = meta.PostMeta.PostMeta()

        post_meta.path = md_path
        post_meta.title = self.result["Title"] if self.result.get("Title") is not None else ""
        post_meta.key_words = _list_from_str(self.result["KeyWords"]) if self.result.get("KeyWords") is not None else []
        post_meta.description = self.result["Description"] if self.result.get("Description") is not None else ""
        post_meta.thumbnail = self.result["Thumbnail"] if self.result.get("Thumbnail") is not None else ""
        post_meta.create_time = _datetime_form_str(self.result["CreateTime"]) if self.result.get("CreateTime") is not None else None
        post_meta.update_time = _datetime_form_str(self.result["UpdateTime"]) if self.result.get("UpdateTime") is not None else None
        post_meta.release_time = _datetime_form_str(self.result["ReleaseTime"]) if self.result.get("ReleaseTime") is not None else None
        post_meta.template = self.result.get("Template") if self.result.get("Template") is not None else None
        post_meta.json = _json_from_str(self.result["JSON"]) if self.result.get("JSON") is not None else {}
        post_meta.markdown = self.markdown_buffer

        if post_meta.title == "":
            post_meta.title = _get_title_from_file(md_path)
        if post_meta.create_time is None:
            post_meta.create_time = _get_create_time_from_file(md_path)
        if post_meta.update_time is None:
            post_meta.update_time = _get_update_time_from_file(md_path)
        if post_meta.release_time is None:
            post_meta.release_time = post_meta.create_time
        return post_meta

    def __f_start(self):
        if self.length < 1:
            self.func = self.__f_finish
            return

        self.func = self.__f_entry

    def __f_entry(self):
        if self.pointer == self.length - 1:
            self.func = self.__f_finish
            return

        if self.text[self.pointer] in ["", " ", "\n", "\r", "\t"]:
            self.pointer += 1
            self.func = self.__f_entry
            return

        if self.text[self.pointer] == "@":
            self.pointer += 1
            self.func = self.__f_key
            return

        self.func = self.__f_markdown

    def __f_key(self):
        if self.text[self.pointer] in ["", " ", "\n", "\r", "\t"]:
            self.pointer += 1
            self.func = self.__f_value
            return

        self.key_buffer += self.text[self.pointer]
        self.pointer += 1
        self.func = self.__f_key

    def __f_value(self):
        if self.text[self.pointer] == "@":
            self.result[self.key_buffer] = self.value_buffer
            self.key_buffer = ""
            self.value_buffer = ""
            self.pointer += 1
            self.func = self.__f_entry
            return

        self.value_buffer += self.text[self.pointer]
        self.pointer += 1
        self.func = self.__f_value

    def __f_markdown(self):
        if self.pointer == self.length - 1:
            self.func = self.__f_finish
            return

        self.markdown_buffer += self.text[self.pointer]
        self.pointer += 1

    def __f_finish(self):
        return


def parse_post_meta(md_path: str) -> meta.PostMeta.PostMeta:
    dfa = ParsePostMetaDFA()
    return dfa.do(md_path)


if __name__ == "__main__":
    post_meta = parse_post_meta("../../../demo/site/栏目4/栏目4-1文章1.md")
    print(post_meta)
