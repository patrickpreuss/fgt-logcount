#!/usr/bin/python
# -*- coding: utf-8 -*-

# todo
# - replacing current logic to dictionaly
#

# debug_mode
#  0: no debug
#  1: simple printing
#  2: printing line number
debug_mode = 0
line_number = 1

# count_period
#  5: hh:mm (per min)
#  2: hh (per hour)
count_period = 2

filename = 'log'

f = open(filename)

pre_time = ""
repeated = 1
pre_attack_name = ""
pre_result = ""

while 1:
	if debug_mode == 2: print line_number
	line = f.readline()
	if not line:
		if debug_mode == 1: print '... final printing'
		print pre_result + ", " + str(repeated)
		break

	# line_sp is used as a parsered line
	line_sp = line.split(" ")
	# time_stamp is for printing as a final result
	time_stamp = line_sp[0].lstrip("date=") + ", " + line_sp[1].lstrip("time=")[:count_period]
	# cur_time is a value to compare with previous result to count up a repeated value
	cur_time = line_sp[1].lstrip("time=")[:count_period]
	# attack_name is an attack name in a current loop
	attack_name = line_sp[18].split("\"")[1]


	if pre_time == cur_time and pre_attack_name == attack_name:
		if line.find("repeated") != -1:
			if debug_mode == 1: print '... repeated repeating'
			repeated = repeated + int(line_sp[len(line_sp)-2]) # [len(line_sp)-2] is repeated number
		else:
			if debug_mode == 1: print '... single repeating'
			repeated = repeated + 1
	cur_result = time_stamp + ", " + attack_name
	if pre_result != "" and pre_result != cur_result:
		if debug_mode == 1: print 'pre:cur = ' + pre_result + ":" + cur_result
		print pre_result + ", " + str(repeated)
		repeated = 1

	# Finalization at the end of the loop
	if debug_mode == 1: print '... finalization'
	pre_time = line_sp[1].lstrip("time=")[:count_period]
	pre_attack_name = attack_name
	pre_result = time_stamp + ", " + attack_name
	line_number = line_number + 1

