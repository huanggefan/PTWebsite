import typing

from info.PostInfo import PostInfo


class DirectoryInfo(object):
    def __init__(self):
        self.url = ""
        self.name = ""

        self.posts: list[PostInfo] = []
        self.all_posts: list[PostInfo] = []

        self.father_node: typing.Optional[DirectoryInfo] = None
        self.child_node: list[DirectoryInfo] = []

        self.render_src = ""
        self.render_dist = ""

    def __str__(self):
        return \
            '''
            url: {}
            name: {}
            posts: {}
            all_posts: {}
            father_node: {}
            child_node: {},
            render_src: {},
            render_dist: {},
            '''.format(
                self.url,
                self.name,
                self.posts,
                self.all_posts,
                self.father_node,
                self.child_node,
                self.render_src,
                self.render_dist,
            )
