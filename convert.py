import datetime
import json
import os
import shutil
import sys
import time

warning = "Usage: convert <log file path> <output file path>"

argvs = sys.argv
if len(argvs) != 3:
	print(warning)
	sys.exit()

log_file_path = os.path.realpath(argvs[1])
ouput_file_path = os.path.realpath(argvs[2])

if not os.path.exists(log_file_path) or not os.path.isfile(log_file_path):
	print("{0} is not a file".format(log_file_path))
	sys.exit()

try:
	output_file = open(ouput_file_path,'w')
except:
  print(warning)
  sys.exit()

key_dict = {
	5 : ["type", "ts", "execute_path", "command", "sha"],
	6 : ["type", "ts", "root_path", "execute_path", "command", "sha"]
}

output_list = []

with open(log_file_path) as f:
	for line in f:
		data_array = line.rstrip().split(",")
		length = len(data_array)

		if length in key_dict:
			line_in_dict = dict(zip(key_dict[length], data_array))
			date_str = line_in_dict["ts"]
			line_in_dict["ts"] = int(time.mktime(datetime.datetime.strptime(date_str, "%Y%m%d-%H%M%S").timetuple()))
			output_list.append(line_in_dict)

output_file.write(json.dumps(output_list, separators=(',',':')))
output_file.close()
