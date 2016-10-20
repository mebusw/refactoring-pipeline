#! encoding=utf8

# Person类拥有标识对象的一个集合。标识有一个域来存放模式和一些值。
# 这个函数的坏味道就是在循环中同时做两件事情。它在寻找重复的identifiers(在dups集合中)，同时寻找需要的但是缺失的模式（在required_schemes）中。程序员经常要在同一个集合对象中做两件事，于是决定使用相同的循环来处理。一个原因是代码要求建立一个循环，如果将它重复两次将会看起来非常丢人。现代的循环构造函数和管道则消除了这个负担。另一个更有害的原因是对于性能的担心。显而易见的很多性能上的热点都会包含循环，并且也有些将循环融合之后性能能够提高的例子。但是这在我们所写的循环中只占了非常小的一部分，因此我们应该遵循编程中的常规准则。 **集中精力于清晰化代码而不是性能，除非你已经有可衡量的巨大的性能问题。** 如果你真有性能方面的问题，则修复问题要优先于清晰化代码，但是这种例子非常少见。
# 剥离一个循环中的两件事情
# http://www.martinfowler.com/articles/refactoring-pipelines/identifiers-class.png
#


class Identifier(object):
    scheme = ''
    value = 0
    is_void = False

    def __init__(self, scheme, is_void):
        self.scheme = scheme
        self.is_void = is_void


class Notification(object):
    error = ''
    def add_error(self, e):
        self.error += e


class Person(object):
    def __init__(self, ids):
        self.ids = ids

    def check_valid_ids(self, required_schemes, note=None):
        note = note or Notification()
        if len(self.ids) < 1: note.add_error("has no ids") 
        
        used = []
        found_required = []
        dups = []
        
        for id in self.ids:
            if id.is_void: continue
            if id.scheme in used:
                dups.append(id.scheme)
            else:
                for req in required_schemes:
                    if id.scheme == req:
                        found_required.append(req)
                        required_schemes.remove(req)
                        continue
                .append(id.scheme)
        
        if len(dups) > 0:
            note.add_error("duplicate schemes: " + ", ".join(dups) + "\n")
        
        if len(required_schemes) > 0:
            missing_names = ""
            for req in required_schemes:
                missing_names += ", " + str(req) if len(missing_names) > 0 else str(req)
            note.add_error("missing schemes: " + missing_names)
        
        return note
 


p = Person([Identifier('agile', False), Identifier('agile', False), Identifier('rup', True), Identifier('kanban', False), Identifier('xp', False), Identifier('pmp', True)])
note = Notification()
p.check_valid_ids(['agile', 'kanban', 'xp', 'dsdm'], note)

print note.error
assert note.error == 'duplicate schemes: agile\nmissing schemes: dsdm'


################
# 提取方法, 拆分循环
# 重复循环，删除双重更新： check_no_duplicate_ids， check_all_required_schemes
# 对非重复检查进行重构  check_no_duplicate_ids()
    # 提取变量, filter(void)
    # map(scheme)
    # 寻找重复部分 self.ids | groupby(lambda x:x) | select(lambda y: (y[0],(y[1]| count))) | where(lambda z: z[1] > 1)
    # 提取方法 duplicates()
# 重构所有必需模式的检查 check_all_required_schemes()
    # 提取变量, filter(void)
    # map(scheme)
    # 捕获那些既在required_schemes列表中并且又存在于来自于ID的那些模式  => 集合交集  found_required = schemes & required_schemes
    # 发现found_required其实是僵尸变量
    # 移除向参数的赋值, 不修改原始变量，改用副本  missing_schemes = set(required_schemes)
    # 差集操作 missing_schemes = set(required_schemes) - set(schemes)
    # 字符串连接操作 '. 'join()
# 整合两个方法
    # 提取公共方法 identity_schemes
    # 内联临时变量
    # 转变为单行条件语句


