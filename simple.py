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



a1 = Author('bill', 'bl', 'uperform')
a2 = Author('jacky', 'j', 'uperform')
a3 = Author('papiJam', 'papi', 'logitech')

assert ['bl', 'j'] == Author.TwitterHandles([a1,a2,a3], 'uperform')