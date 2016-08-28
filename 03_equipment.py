data = {
'products': ['snow-blower', 'snow-shovel'],
'regions': ['boston', 'miami'],
'offerings': [
    {'region':'boston', 'supported': 'snow-blower', 'supplied': 'snow-blower'},
    {'region':'boston', 'supported': 'snow-blower', 'supplied': 'snow-shovel'},
    {'region': 'miami', 'supported': 'snow-blower', 'supplied': 'snow-shovel'},
    ]
}

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