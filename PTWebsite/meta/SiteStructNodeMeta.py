import typing


class SiteStructNodeMeta(object):
    def __init__(self):
        self.father_node: typing.Optional[SiteStructNodeMeta] = None
        self.child_node: list[SiteStructNodeMeta] = []
        self.posts: list[str] = []
        self.name = ""
        self.path = ""

    def __dict__(self):
        return {
            "father_node": self.father_node,
            "child_node":  self.child_node,
            "posts":        self.posts,
            "name":        self.name,
            "path":        self.path,
        }

    def __str__(self):
        return \
            '''
            father_node: {}
            child_node: {}
            post: {}
            name: {}
            path: {}
            '''.format(
                self.father_node,
                self.child_node,
                self.posts,
                self.name,
                self.path,
            )
