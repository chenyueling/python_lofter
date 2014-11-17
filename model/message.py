__author__ = 'chenyueling'

import json



class ArticleMessage(object):
    def __init__(self, link, title, audience='all'):
        self.article = {
            'title': title,
            'link': link
        }
        self.audience = audience
        self.type = 'ARTICLE'

    def get_json(self):
        return json.dumps(self.__dict__)

