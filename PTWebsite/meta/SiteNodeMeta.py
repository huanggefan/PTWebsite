import typing


class SiteNodeMeta(object):
    def __init__(self):
        self.father_node: typing.Optional[SiteNodeMeta] = None
        self.child_node: list[SiteNodeMeta] = []

        self.post_files: list[str] = []
        self.all_post_files: list[str] = []

        self.name = ""
        self.path = ""

    def __dict__(self):
        return {
            "father_node":    self.father_node,
            "child_node":     self.child_node,
            "post_files":     self.post_files,
            "all_post_files": self.all_post_files,
            "name":           self.name,
            "path":           self.path,
        }

    def __str__(self):
        return \
            '''
            father_node: {}
            child_node: {}
            post_files: {}
            all_post_files: {}
            name: {}
            path: {}
            '''.format(
                self.father_node,
                self.child_node,
                self.post_files,
                self.all_post_files,
                self.name,
                self.path,
            )

    def print(self):
        this_str = '''path: {}, name: {}, post_files: {}'''.format(self.path, self.name, self.post_files)
        print(this_str)
        for node in self.child_node:
            node.print()
