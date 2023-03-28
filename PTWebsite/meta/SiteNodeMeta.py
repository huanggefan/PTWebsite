import typing


class SiteNodeMeta(object):
    def __init__(self):
        self.name: str = ""
        self.path: str = ""

        self.key_words: list[str] = []
        self.description: str = ""
        self.thumbnail: str = ""
        self.template: str = ""
        self.customer_meta: dict = {}

        self.post_files: list[str] = []

        self.father_node: typing.Optional[SiteNodeMeta] = None
        self.child_node: list[SiteNodeMeta] = []

    def __str__(self):
        return \
            '''
            name: {}
            path: {}
            key_words: {}
            description: {}
            thumbnail: {}
            template: {}
            customer_meta: {}
            post_files: {}
            father_node: {}
            child_node: {}
            '''.format(
                self.name,
                self.path,
                self.key_words,
                self.description,
                self.thumbnail,
                self.template,
                self.customer_meta,
                self.post_files,
                self.father_node,
                self.child_node
            )

    def dict(self):
        return {
            "key_words":     self.key_words,
            "description":   self.description,
            "thumbnail":     self.thumbnail,
            "template":      self.template,
            "customer_meta": self.customer_meta,
        }
