# PTWebsite

## build

```shell
pip install -r requirements.txt
pyinstaller -F PTWebsite/__main__.py --name=PTWebsite
```

## usage

generate website

```shell
PTWebsite -r ./demo_site
```

start basic http server after generate website

```shell
PTWebsite -r ./demo_site -s
```

show help information

```shell
PTWebsite -h
```

show version information

```shell
PTWebsite -v
```

## your site directory

something like [demo](./demo)

site root at [demo](./demo)

markdown files in [site](./demo/site)

markdown cover files also in [site](./demo/site), same directory, name as markdown file

png, jpg and others in [site/statics](./demo/site/statics)

templates in [templates](./demo/templates)

site meta info at [meta.json](./demo/meta.json)

generate output in[output](./demo/output)

```
 --- [ROOT]
 ---- ---- site
 ---- ---- ---- statics
 ---- ---- ---- [.MD FILES]
 ---- ---- ---- [OTHER_DIRECTORY]
 ---- ---- templates
 ---- ---- output
 ---- ---- meta.json
```

## your templates

something like [demo](./demo/templates)

**directory.html** and **post.html** is must, others not must.

one markdown file render as a post, one directory render as a post directory.

SiteInfo and DirectoryInfo use to render directory, SiteInfo and PostInfo use to render post.

## render info

```python
import typing
import datetime


class SiteInfo(object):
    def __init__(self):
        self.name = ""
        self.owner = ""
        self.key_words: list[str] = []
        self.description = ""
        self.customer_meta = {}


class DirectoryInfo(object):
    def __init__(self):
        self.name = ""
        self.url = ""

        self.key_words: list[str] = []
        self.description: str = ""

        self.thumbnail_url = ""
        self.thumbnail_alt = ""

        self.template: str = ""

        self.customer_meta: dict = {}

        self.posts: list[PostInfo] = []
        self.all_posts: list[PostInfo] = []

        self.father_node: typing.Optional[DirectoryInfo] = None
        self.child_node: list[DirectoryInfo] = []


class PostInfo(object):
    def __init__(self):
        self.url = ""

        self.title = ""
        self.key_words: list[str] = []
        self.description = ""

        self.thumbnail_url = ""
        self.thumbnail_alt = ""

        self.create_time: typing.Optional[datetime.datetime] = None
        self.update_time: typing.Optional[datetime.datetime] = None
        self.release_time: typing.Optional[datetime.datetime] = None

        self.template = ""

        self.json = {}

        self.markdown = ""
        self.html = ""


info_to_render_directory = {
    "site":      SiteInfo,
    "directory": DirectoryInfo,
}
info_to_render_post = {
    "site": SiteInfo,
    "post": PostInfo,
}
info_to_render_site_root_post = {
    "site": SiteInfo,
    "root": DirectoryInfo,
    "post": PostInfo,
}
```

## post meta key

1. Title
2. KeyWords
3. Description
4. Thumbnail
5. CreateTime
6. UpdateTime
7. ReleaseTime
8. Template
9. JSON
