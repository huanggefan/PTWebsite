import typing


class SiteNodeMeta(object):
    def __init__(self):
        self.father_node: typing.Optional[SiteNodeMeta] = None
        self.child_node: list[SiteNodeMeta] = []

        self.post_files: list[str] = []

        self.name = ""
        self.path = ""

    def __str__(self):
        return \
            '''
            father_node: {}
            child_node: {}
            post_files: {}
            name: {}
            path: {}
            '''.format(
                self.father_node,
                self.child_node,
                self.post_files,
                self.name,
                self.path,
            )
