#/usr/bin/env python

class Rational:
    def __init__(self,x,y):
        number = x
        if y == 0:
            raise ZeroDivisionError()
        else:
            denom = y

try:
    rat1 = Rational(4,1)
    rat2 = Rational(3,0)
except:
    print("Cannot have a 0 for the denominator")