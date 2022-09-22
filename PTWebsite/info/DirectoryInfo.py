import info.PostInfo


class DirectoryInfo(object):
    def __init__(self):
        self.url = ""
        self.name = ""
        self.posts: list[info.PostInfo.PostInfo] = []
        self.all_posts: list[info.PostInfo.PostInfo] = []

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
