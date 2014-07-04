#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

filename = 'log'

a = np.loadtxt(filename, delimiter=" ", dtype={\
'names':('date', 'time', 'itime', 'devname', 'devid', 'logid', 'type', 'subtype', 'eventtype', 'level', 'vd', 'severity', 'srcip', 'dstip', 'sessionid', 'action', 'proto', 'service', 'attack', 'srcport', 'dstport', 'attackid', 'profile', 'ref', 'incidentserialno', 'msg1', 'msg2', 'msg3', 'msg4', 'msg5', 'msg6'),\
'formats':('S99', 'S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','S99','i','S99')})


print a['attack']
