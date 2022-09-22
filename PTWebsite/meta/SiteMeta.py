class SiteMeta(object):
    def __init__(self):
        self.name = ""
        self.owner = ""
        self.key_words: list[str] = []
        self.description = ""
        self.customer_meta = {}

    def __dict__(self):
        return {
            "name":          self.name,
            "owner":         self.owner,
            "key_words":     self.key_words,
            "description":   self.description,
            "customer_meta": self.customer_meta,
        }

    def __str__(self):
        return \
            '''
            name: {}
            owner: {}
            key_words: {}
            description: {}
            customer_meta: {}
            '''.format(
                self.name,
                self.owner,
                self.key_words,
                self.description,
                self.customer_meta,
            )
