__author__ = 'chenyueling'

import json


class ArticleMessage(object):
    def __init__(self, link, title, summary=None, audience='all'):
        self.article = {
            'title': title,
            'link': link,
        }

        if summary != None:
            self.article['summary'] = summary
        self.audience = audience
        self.type = 'ARTICLE'

    def get_json(self):
        return json.dumps(self.__dict__)


#Test
print ArticleMessage('link','title','summary').get_json()