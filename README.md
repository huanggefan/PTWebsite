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
        self.url = ""
        self.name = ""
        self.posts: list[PostInfo] = []
        self.all_posts: list[PostInfo] = []


class PostInfo(object):
    def __init__(self):
        self.url = ""
        self.title = ""
        self.key_words: list[str] = []
        self.description = ""
        self.create_time: typing.Optional[datetime.datetime] = None
        self.update_time: typing.Optional[datetime.datetime] = None
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
```