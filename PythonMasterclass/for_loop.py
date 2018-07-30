number = "1,454,23,54,2,3453,245"
for i in range(0,len(number)):
    if number[i] in "0123456789":
        print (number[i],end="")