import typing
import datetime


class PostMeta(object):
    def __init__(self):
        self.path = ""

        self.title = ""
        self.key_words: list[str] = []
        self.description = ""

        self.create_time: typing.Optional[datetime.datetime] = None
        self.update_time: typing.Optional[datetime.datetime] = None
        self.release_time: typing.Optional[datetime.datetime] = None

        self.markdown = ""

    def __dict__(self):
        return {
            "path":         self.path,
            "title":        self.title,
            "key_words":    self.key_words,
            "description":  self.description,
            "create_time":  self.create_time,
            "update_time":  self.update_time,
            "release_time": self.release_time,
            "markdown":     self.markdown,
        }

    def __str__(self):
        return \
            '''
            path: {} 
            title: {}
            key_words: {}
            description: {}
            create_time: {}
            update_time: {}
            release_time: {}
            '''.format(
                self.path,
                self.title,
                self.key_words,
                self.description,
                self.create_time,
                self.update_time,
                self.release_time,
            )
