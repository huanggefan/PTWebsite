class SiteInfo(object):
    def __init__(self):
        self.name = ""
        self.owner = ""
        self.key_words: list[str] = []
        self.description = ""
        self.customer_meta = {}

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
