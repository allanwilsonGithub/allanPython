def take(num, lyst):
    rlist = []
    for i in range(num,0):
        rlist.append(lyst[i])
    return rlist

def drop(num, lyst):
    rlist = lyst
    for i in range(num,0):
        rlist.remove(lyst[i])
    return rlist

names = ['Raymond','Cynthia','David','Jennifer','Clayton']
somenames = take(-3,names)
print(somenames)
names = drop(-3,names)
print(names)