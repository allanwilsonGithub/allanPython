#!/usr/bin/env python

import os
import sys

files = ["leave_the_bourbon_on_the_shelf.txt",
         "gotton.txt"]
strings = ["satisfied",
           "face",
           "the"]

def get_file(file_to_search):
    try:
        assert os.path.isfile(file_to_search)
    except:
        print("File does not exist.")
        sys.exit(1)
    f = open(file_to_search, 'r')
    lines = f.readlines()
    return lines

def search_for_string(search_string,lines):
    strings_found = []
    for line in lines:
        if search_string in line:
            strings_found.append(line)
    return strings_found

def display_result(strings_found):
    count = 0
    for result in strings_found:
        count += 1
        print (str(count) + ": " + result.strip())

    print("Total hits for \"" + string +"\": " + str(count))

for file in files:
    print("===== " + file + " =====")
    lines = get_file(file)
    for string in strings:
        strings_found = search_for_string(string,lines)
        display_result(strings_found)