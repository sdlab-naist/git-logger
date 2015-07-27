import os
import shutil
import sys

argvs = sys.argv
if len(argvs) != 2:
	print("Usage: convert <log file path>")
	sys.exit()

log_file_path = os.path.realpath(argvs[1])

if not os.path.exists(log_file_path) or not os.path.isfile(log_file_path):
	print("{0} is not a file".format(log_file_path))
	sys.exit()

converted_log_path = ""
f = open(converted_log_path,'a')

with open(log_file_path) as f:
	for line in f:
		data_array = line.split(",")
		f.write(line)

f.close()
