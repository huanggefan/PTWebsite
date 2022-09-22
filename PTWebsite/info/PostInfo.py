import typing
import datetime


class PostInfo(object):
    def __init__(self):
        self.url = ""
        self.title = ""
        self.key_words: list[str] = []
        self.description = ""
        self.create_time: typing.Optional[datetime.datetime] = None
        self.update_time: typing.Optional[datetime.datetime] = None
        self.markdown = ""
        self.html = ""

    def __str__(self):
        return \
            '''
            url: {}
            title: {}
            key_words: {}
            description: {}
            create_time: {}
            update_time: {}
            markdown: {}
            html: {}
            '''.format(
                self.url,
                self.title,
                self.key_words,
                self.description,
                self.create_time,
                self.update_time,
                self.markdown,
                self.html,
            )
