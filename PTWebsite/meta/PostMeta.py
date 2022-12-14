import typing
import datetime


class PostMeta(object):
    def __init__(self):
        self.path = ""

        self.title = ""
        self.key_words: list[str] = []
        self.description = ""

        self.cover_path = ""

        self.create_time: typing.Optional[datetime.datetime] = None
        self.update_time: typing.Optional[datetime.datetime] = None
        self.release_time: typing.Optional[datetime.datetime] = None

        self.markdown = ""

    def __str__(self):
        return \
            '''
            path: {} 
            title: {}
            key_words: {}
            description: {}
            cover_path: {}
            create_time: {}
            update_time: {}
            release_time: {}
            markdown: {}
            '''.format(
                self.path,
                self.title,
                self.key_words,
                self.description,
                self.cover_path,
                self.create_time,
                self.update_time,
                self.release_time,
                self.markdown,
            )
