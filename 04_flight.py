#! encoding=utf8

# 将飞机晚点信息汇总的代码
# 这个循环通过总结航班数据中目的地机场（dest）并且计算取消率来定义延误。这个处理的核心就是通过目的地来对航班数据分组，这正好适用管道中的分组操作。

data = [
    {
    "origin":"BOS","dest":"LAX","date":"2015-01-12",
    "number":"25","carrier":"AA","delay":1.0,"cancelled":False
    },
    {
    "origin":"BOS","dest":"LAX","date":"2015-01-13",
    "number":"25","carrier":"AA","delay":2.0,"cancelled":False
    },
    {
    "origin":"BOS","dest":"LAX","date":"2015-01-14",
    "number":"25","carrier":"AA","delay":2.0,"cancelled":True
    },
    {
    "origin":"SZN","dest":"PEK","date":"2015-01-15",
    "number":"25","carrier":"AA","delay":3.0,"cancelled":False
    },
    {
    "origin":"SZN","dest":"PEK","date":"2015-01-16",
    "number":"25","carrier":"AA","delay":1.0,"cancelled":False
    },
]


def airportData():
    count = {}
    cancellations = {}
    totalDelay = {}

    for row in data:
        airport = row['dest']
        if not count.has_key(airport):
            count[airport] = 0
            cancellations[airport] = 0
            totalDelay[airport] = 0
        
        count[airport] += 1

        if row['cancelled']:
            cancellations[airport] += 1
        else:
            totalDelay[airport] += row['delay']

    result = {}
    for i in count:
        result[i] = {}
        result[i]['meanDelay'] = totalDelay[i] * 1.0 / (count[i] - cancellations[i])
        result[i]['cancellationRate'] = cancellations[i] * 1.0 / count[i]
    
    return result

print airportData()
assert airportData() == {'LAX': {'cancellationRate': 0.3333333333333333, 'meanDelay': 1.5}, 'PEK': {'cancellationRate': 0.0, 'meanDelay': 2.0}}

################
# working = _.groupBy(data, r => r.dest)
# map `Count`变量记录对每个目的地机场有多少飞行记录。  rows.length,
# 处理取消业务变量 cancellations: rows.filter(r => r.cancelled).length,
# 提取方法
# totalDelay: rows.filter(r => !r.cancelled).reduce((acc,each) => acc + each.delay, 0
	# 首先使用map会让它更易读 totalDelay: rows.filter(r => !r.cancelled).map(r => r.delay).reduce((a,b) => a + b)
# 重命名将Lambda替换为`summarize`函数
# 第二个循环,通过map映射去计算它的两个值
# 内联临时变量, 重命名和清理工作

