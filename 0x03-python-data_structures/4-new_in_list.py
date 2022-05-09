#!/usr/bin/python3
def new_in_list(my_list, idx, element):
	MY_LIST = my_list
	if idx < 0:
		return MY_LIST
	if idx >= len(my_list):
		return MY_LIST
	for x in range(len(MY_LIST)):
		if x == idx:
			MY_LIST[x] = element
			return MY_LIST
	