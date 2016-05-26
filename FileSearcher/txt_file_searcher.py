#!/usr/bin/env python

#Variables:
file_to_search = "D:\\DATA\\git\\allanPython\\FileSearcher\\leave_the_bourbon_on_the_shelf.txt"
search_string = "satisfied"
strings_found = []

#Open the file
f = open(file_to_search, 'r')
lines = f.readlines()

#Search the file for each string
for line in lines:
    if search_string in line:
        strings_found.append(line)

#Display the results
for result in strings_found:
    print result