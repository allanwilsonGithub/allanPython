#!/usr/bin/env python

class Student:
    #fields - name, id, grades(list)
    grades = []
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def addGrade(self,grade):
        self.grades.append(grade)

    def showGrades(self):
        grds = ''
        for grade in self.grades:
            grds += str(grade) + ' '
        return grds

    def __str__(self):
        return "Name: " + self.name + "\n" + \
               "Id: " + self.id + "\n" + \
               "Grades: " + self.showGrades()

    def averageGrades(self):
        totalGrades = 0
        for grade in self.grades:
            totalGrades += grade
        return totalGrades / len(self.grades)


stu1 = Student('Jones','123')
stu1.addGrade(88)
stu1.addGrade(84)
stu1.addGrade(91)
print(stu1.showGrades())

print str(stu1)
print stu1.averageGrades()