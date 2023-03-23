import typing
import datetime


class PostInfo(object):
    def __init__(self):
        self.url = ""

        self.title = ""
        self.key_words: list[str] = []
        self.description = ""

        self.thumbnail_url = ""
        self.thumbnail_alt = ""

        self.create_time: typing.Optional[datetime.datetime] = None
        self.update_time: typing.Optional[datetime.datetime] = None
        self.release_time: typing.Optional[datetime.datetime] = None

        self.template = ""

        self.json = {}

        self.markdown = ""
        self.html = ""

        self.render_src = ""
        self.render_dist = ""

    def __str__(self):
        return \
            '''
            url: {}
            title: {}
            key_words: {}
            description: {}
            thumbnail_url: {}
            thumbnail_alt: {}
            create_time: {}
            update_time: {}
            release_time: {}
            markdown: {}
            json: {}
            html: {}
            render_src: {},
            render_dist: {},
            '''.format(
                self.url,
                self.title,
                self.key_words,
                self.description,
                self.thumbnail_url,
                self.thumbnail_alt,
                self.create_time,
                self.update_time,
                self.release_time,
                self.json,
                self.markdown,
                self.html,
                self.render_src,
                self.render_dist,
            )
