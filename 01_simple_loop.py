#! encoding=utf8
from pipe import *

class Author(object):
    def __init__(self, Name, TwitterHandle, Company):    
        self.Name = Name
        self.TwitterHandle = TwitterHandle
        self.Company = Company

    @staticmethod
    def TwitterHandles(authors, company):
        result = []
        for a in authors:
            if a.Company == company:
                handle = a.TwitterHandle
                if handle != None:
                    result.append(handle)
        return result


############
a1 = Author('Bill Li', 'bill', 'uperform')
a2 = Author('Jacky Shen', 'jacky', 'uperform')
a3 = Author('Papi Jam', 'papi', 'logitech')

assert ['bill', 'jacky'] == Author.TwitterHandles([a1,a2,a3], 'uperform')




#############
# 抽取变量
# filter, map, filter
# 调整管道的顺序，无副作用

        # return filter(lambda h: h != None, 
        #             map(lambda a: a.TwitterHandle, 
        #                 filter(lambda a: a.Company == company, 
        #                     authors)))


        # return authors | where(lambda a: a.Company == company) | select(lambda a: a.TwitterHandle) | where(lambda handle: handle != None) | as_list
        
