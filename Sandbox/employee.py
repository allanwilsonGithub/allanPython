#/usr/bin/env python

class Employee:
    '''This is the base class'''
    def __init__(self, name, payRate):
        self.name = name
        self.payRate = payRate

    def __str__(self):
        return self.name + ", " + str(self.payRate)

    def pay(self, hoursWorked):
        return self.payRate * hoursWorked

class Manager(Employee):
    '''This is the derived class'''
    def __init__(self, name, payRate, isSalaried):
        Employee.__init__(self, name, payRate)
        self.salaried = isSalaried

    def __str__(self):
        retStr = Employee.__str__(self)
        retStr += " salaried: " + str(self.salaried)
        return retStr

    def pay(self, hoursWorked):
        if self.salaried:
            return self.payRate
        else:
            return self.payRate * hoursWorked

Mark = Employee('Mark', 34)
print (Mark.pay(20))

Manager1 = Manager("Jane", 40, False)
print(Manager1.pay(20))