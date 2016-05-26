#!/usr/bin/env python

class Name:
    #constructor method - instantiation
    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last

    #to-string method
    def __str__(self):
        return self.first + ' ' + self.middle + ' ' + self.last

    def lastFirst(self):
        return self.last + ' ' + self.first + ' ' + self.middle

    def printItNicely(self):
        return "The first name is: " + self.first + '\n' + "The middle name is: " + self.middle + '\n' + "The last name is: " + self.last

    def initials(self):
        return "Initials: " + self.first[0] + ' ' + self.middle[0] + ' ' + self.last[0]

aName = Name('Mary','Elizabeth','Smith')
bName = Name('Bob','John','Wilson')
cName = Name('Mark','Philip','Paul')

print cName
print "==============================="
print("Using lastFirst method gives: " + cName.lastFirst())
print "================================"
print(cName.printItNicely())
print "================================="
print ("aName Initials: " + aName.initials())
print ("bName Initials: " + bName.initials())
print ("cName Initials: " + cName.initials())