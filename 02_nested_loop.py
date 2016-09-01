#! encoding=utf8

# Readers <-> dataOnDate <-> Books
# 重构一个简单的双重嵌套循环。假设我有一个在线系统允许读者看书。我有一个数据服务，它可以告诉我在某个特殊的日期每个读者读的哪些书。这个数据服务返回一些哈希，键是读者ID，而值是书籍ID的集合。


def getReadersOfBooks(readers, books, date):
    result = set()
    data = dataService.getBooksReadOn(date)

    for e in data.items():
        for bookId in books:
            key, value = e[0], e[1]
            if bookId in value and key in readers:
                result.add(e[0])
    return result

#######################
#抽取变量
# filter(readers.contains(e.key))
# intersection(e.value, books)
# 内联临时变量
# map(key)
# 提取方法hasIntersection()


