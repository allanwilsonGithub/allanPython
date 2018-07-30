__author__ = "Allan Wilson"

age = 24
height = 178
print("My age is " + str(age) + " years")

print("My age is {0} years. My height is {1} centimetres".format(age,height))

print("There are {0} days in {1}, {2} and {3}".format(31, "January", "February", "March"))

print("""Sky: {0}
Ground: {1}
Crap: {1}
Water: {0}
""".format("Blue","Brown"))

for i in range (1,12):
    print ("No. %2d squared is %4d and cubed is %4d" %(i,i ** 2, i**3))

print("Pi is approx. %12.50f" % (22/7))

for i in range (1,12):
    print ("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i,i ** 2, i**3))

parrot = "Norwegian blue"
