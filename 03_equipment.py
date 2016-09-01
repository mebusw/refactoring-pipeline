#! encoding=utf8

# 给不同地区提供装备。当你请求一些装备时，你可能能得到完全满足需要的装备，但是经常你会的得到一个能够满足你大部分要求的替代品，但或许没那么好。我们用一个更容易联想的例子：你在波士顿，你想要一个吹雪机，但是如果在商店里没有吹雪机，你可能会得到一个雪铲。但是如果你是在迈阿密，他们甚至根本不提供吹雪机，所以你只会得到雪铲。我们通过以下三个类来描述这个数据模型。
# http://www.martinfowler.com/articles/refactoring-pipelines/equip-offering-classes.png

data = {
'products': ['snow-blower', 'snow-shovel'],
'regions': ['boston', 'miami'],
'offerings': [
    {'region':'boston', 'supported': 'snow-blower', 'supplied': 'snow-blower'},
    {'region':'boston', 'supported': 'snow-blower', 'supplied': 'snow-shovel'},
    {'region': 'miami', 'supported': 'snow-blower', 'supplied': 'snow-shovel'},
    ]
}

class Equipment(object):
    def AllOfferings(region):
        return []
        
equipment = Equipment()        

####################################

def calc():
    checkedRegions = set()
    for o1 in equipment.AllOfferings():
        r = o1.Region
        if r in checkedRegions.Contains(r):
            continue
        
        possPref = None
        for o2 in equipment.AllOfferings(r):
            if o2.isPreferred:
                possPref = o2
                break
            else:
                if o2.isMatch or possPref == None:
                    possPref = o2
        possPref.isPreferred = True
        checkedRegions.Add(r)

calc()        



##################
#抽取变量
# map  循环的第一部分。它有一个控制变量checkedRegions, 循环语句使用这个变量来标记已经处理过的`regions`来避免多次处理。 我感觉到了一些不好的味道，但是它也建议loop变量o1只是用于获取`region r`的一个垫脚石。
# checkedRegions => distinct
# possPref  内层循环=> 提取方法 possiblePreference()
    # break => return
    # FirstOrDefault(o => o.isPreferred);
    # allOfferings.LastOrDefault(o => o.isMatch);
    # First();
    # 重命名
    # 空结合操作符`??` / OR
# 回到外层  Select(x->possiblePreference())

# equipment.AllOfferings()
#     .Select(o => o.Region)
#     .Distinct()
#     .Select(r => possiblePreference(equipment, r))
#     .ToList()  # 副作用
#     .ForEach(o => o.isPreferred = true)
#     ;
# }