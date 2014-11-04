#!/usr/bin/python
# coding=utf-8
__author__ = 'chenyueling'


import json
import urllib2

class Person(object):
    def __init__(self,name,age,fuck):
        self.name = name
        self.age = age
        self.fuck = fuck
        self.list = [{'1':'1'},{'2':'2'},{'3':{'xxx':'xxx'},'4':{'a':'v'}}]
    def __repr__(self):
        return 'Person Object name : %s , age : %d' % (self.name,self.age)

fuck = {'hongxiyu':'1','chenyueling':'2'}
p = Person('Peter',22,fuck)



#这个是打印对象的值
#print p.__dict__
d = {'p':p.__dict__}
d.update(p.__dict__)

resp = urllib2.urlopen('https://gist.githubusercontent.com/chenyueling/3d17043439a82e31e33f/raw/302703975c1a09243b0094306dfd9377f9f9420e/ACTION_SERVICE_CREATE.json')

jsonStr = resp.read()

print jsonStr
#dir 是打印出对象的属性
print dir(p)

#格式化对象为json 字符串的时候 indent 可以将jsonString 格式化输出 indent 后面的参数是带
jsonstr = json.dumps(d,indent=4)

print {'indent':4}
print type(jsonstr)
print type({'indent':4})
print jsonstr

# json.loads(jsonStr) 这个是将json 字符串作为
#另一个比较有用的dumps参数是skipkeys，默认为False。 dumps方法存储dict对象时，key必须是str类型，如果出现了其他类型的话，那么会产生TypeError异常，如果开启该参数，设为True的话，则会比较优雅的过度。
print json.loads(jsonStr)



print d
