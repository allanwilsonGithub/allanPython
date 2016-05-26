#!/usr/bin/env python

class Person:
    def __init__ (self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return self.name + ' ' + self.age + ' ' + self.sex

Brian = Person('Brian','Male','22')
Jill = Person('Jill','Female','52')

print "Brian Age: " + Brian.age
print "Jill Age: " + Jill.age

print "Brain stats: " + str(Brian)