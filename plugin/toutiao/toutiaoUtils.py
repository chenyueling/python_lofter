__author__ = 'chenyueling'

import urllib2
import json

hostUrl = 'http://www.toutiao.com'

NEWS_URL = hostUrl + '/toutiao/api/article/recent/'

GALLERY_URL = hostUrl + '/toutiao/api/gallery/recent/'

TITLE = 'title'

SUMMARY = 'summary'

LINK = 'link'


def get_toutiao_news():
    request = urllib2.Request(NEWS_URL)

    response = urllib2.urlopen(request)
    jsonStr = response.read()

    news = json.loads(jsonStr)

    if news['message'] == 'success':
        data = news['data']
        i = 0
        article = {}
        for item in data:
            print item['title']
            print item['favorite_count']
            print item['display_url']
            if i < item['favorite_count']:
                i = item['favorite_count']
                article[TITLE] = item['title']
                # article['favorite_count'] = item['favorite_count']
                article[LINK] = item['display_url']
                article[SUMMARY] = item['abstract']
    return article


def get_toutiao_gallery():
    request = urllib2.Request(GALLERY_URL)
    response = urllib2.urlopen(request)
    jsonStr = response.read()
    gallery = json.loads(jsonStr)
    if gallery['message'] == 'success':
        data = gallery['data']
        for item in data:
            if item['desc'] != None and item['desc'] != '':
                article = {TITLE: item['desc'], LINK: hostUrl + item['share_url']}
                return article

#Test
#print get_toutiao_news()
#print get_toutiao_gallery()