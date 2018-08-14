#!/usr/bin/env python

import file_searcher_test_tool

print "Which tool do you want to use ?...\n1. FileSearcher\n2. MachinePinger"
tool_choice = int(raw_input())

if tool_choice == 1:
	file_searcher_test_tool.search_files()

elif tool_choice == 2:
	machine_pinger()

else:
	print "Wrong choice. Goodbye!!!"