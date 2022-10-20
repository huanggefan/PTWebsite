from info.PostInfo import PostInfo


class DirectoryInfo(object):
    def __init__(self):
        self.url = ""
        self.name = ""

        self.posts: list[PostInfo] = []
        self.all_posts: list[PostInfo] = []

    def __str__(self):
        return \
            '''
            url: {}
            name: {}
            posts: {}
            all_posts: {}
            '''.format(
                self.url,
                self.name,
                self.posts,
                self.all_posts,
            )
