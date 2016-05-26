#!/usr/bin/env python

class Person:
    def __init__ (self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' ' + self.sex

    def changeName(self,name):
        self.name = name

    def changeAge(self):
        self.age = self.age + 1

Brian = Person('Brian','Male','22')
Jill = Person('Jill','Female','52')

person1 = Person('Jane Doe','F',23)
person2 = Person('Bob Smith','M',55)

print ("Person2: " + str(person2))
person2.changeAge()
print ("Person2: " + str(person2))

print ('Person2: ' + str(person2))
person2.changeName('Bob Hoskins')
print ('Person2 (new): ' + str(person2))