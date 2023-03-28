import typing

from info.PostInfo import PostInfo


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

        self.render_src = ""
        self.render_dist = ""

    def __str__(self):
        return \
            '''
            name: {}
            url: {}
            key_words: {}
            description: {}
            thumbnail_url: {}
            thumbnail_alt: {}
            template: {}
            customer_meta: {}
            posts: {}
            all_posts: {}
            father_node: {}
            child_node: {},
            render_src: {},
            render_dist: {},
            '''.format(
                self.name,
                self.url,
                self.key_words,
                self.description,
                self.thumbnail_url,
                self.thumbnail_alt,
                self.template,
                self.customer_meta,
                self.posts,
                self.all_posts,
                self.father_node,
                self.child_node,
                self.render_src,
                self.render_dist,
            )
