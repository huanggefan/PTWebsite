import typing
import datetime


class PostMeta(object):
    def __init__(self):
        self.path = ""

        self.title = ""
        self.key_words: list[str] = []
        self.description = ""

        self.thumbnail = ""

        self.create_time: typing.Optional[datetime.datetime] = None
        self.update_time: typing.Optional[datetime.datetime] = None
        self.release_time: typing.Optional[datetime.datetime] = None

        self.template = ""

        self.json = {}

        self.markdown = ""

    def __str__(self):
        return \
            '''
            path: {} 
            title: {}
            key_words: {}
            description: {}
            thumbnail: {}
            create_time: {}
            update_time: {}
            release_time: {}
            json: {}
            markdown: {}
            '''.format(
                self.path,
                self.title,
                self.key_words,
                self.description,
                self.thumbnail,
                self.create_time,
                self.update_time,
                self.release_time,
                self.json,
                self.markdown,
            )
