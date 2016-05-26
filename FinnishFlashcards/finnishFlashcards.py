#!/usr/bin/env python

flashcard_dict ={}
separator ='++separator++'


inputFile = open('finnishFlashcardsInput.txt','r')
for line in inputFile.readlines():
    print line.split(separator)[0]