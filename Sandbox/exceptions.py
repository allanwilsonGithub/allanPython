#/usr/bin/env python
try:
    num1 = int(raw_input("Enter number1: "))
    num2 = int(raw_input("Enter number2: "))
except ValueErrordasf:
    print("Did you really enter a number?")

try:
    print ("Num1 / Num2 = ") + str(num1/num2)
except ZeroDivisionError:
    print("Cannot devide by 0")
except:
    print("Some other error")

filename = raw_input("Enter filename to open: ")
try:
    file = open(filename, 'r')
except IOError:
    print("That's not a filename!")
