#!/usr/bin/env python

class Robot:
    def __init__(self, colour, size, name, metal):
        self.colour = colour
        self.size = size
        self.name = name
        self.metal = metal

    def __str__(self):
        return self.name + " is a " + self.size + " " + self.colour + " robot made of " + self.metal + "."

    def changeColour(self,colour):
        self.colour = colour

Marvin = Robot('blue','big','Marvin','steel')
Susie = Robot('purple',
              'small',
              'Susie',
              'aluminium')

print(Susie)
print(Marvin)

Susie.changeColour('green')
print(Susie)