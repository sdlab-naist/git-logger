import os
import shutil
import sys

argvs = sys.argv
if len(argvs) != 3:
  print("Usage: logger-organizer <git_history path> <output dir path>")
  sys.exit()

history_path = os.path.realpath(argvs[1])
output_dir_path = os.path.realpath(argvs[2])

if not os.path.exists(history_path) or not os.path.isfile(history_path):
  sys.exit()

if os.path.exists(output_dir_path):
  print("dir already exists. do you want to overwrite it? y/n")
  input_line = raw_input()
  if input_line != "y":
    sys.exit()
  else:
    shutil.rmtree(output_dir_path)

os.mkdir(output_dir_path)

last_path = ""
with open(history_path) as f:
  for line in f:
    line_array = line.split(",")
    if line_array[0] == "LOG":
      if len(line_array) == 5:
        line_array.insert(2, line_array[2])
      output_path = "{0}/{1}.csv".format(output_dir_path, os.path.basename(line_array[2]));
      f = open(output_path,'a')
      f.write(",".join(line_array))
      f.close()
      last_path = output_path
    elif last_path != "":
      f = open(last_path,'a')
      f.write(line)
      f.close()
      pass
