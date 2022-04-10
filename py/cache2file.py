#!/usr/bin/python
# -*- coding: ascii -*-

######################################
# by akleemans, 12/12/12
# modified by graco, 04/12/18
# Extracts a file (for example mp3)
# from a chrome about:cache HTML-file.
######################################

import time
import sys


if len(sys.argv) != 2: print "[+] Please provide filename as argument."
else: filename = sys.argv[1]

print "[+] Converting", filename
t1 = time.time()

file_ext = filename[filename.find('.'):filename.rfind('.')]

source = open(filename, 'rb')
target = open(filename[:filename.find('.')]+file_ext, 'wb')

content = source.read().split("</pre><hr><pre>")[2].split("\n")
source.close()

for line in range(len(content)-1):
	l = content[line].split("  ")[0].split(":")[-1].strip()
	
	hexas = l.split()
	for ff in hexas:
		target.write(ff.decode('hex'))
target.close()

print "[+] Wrote file in", round(time.time()-t1, 2), "s"

