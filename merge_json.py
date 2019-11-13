'''

Hi man, thought I'd start with a joke to make your day...
but the only programming joke that I know is my code,
please enjoy the joke. :")

'''


import os
import glob
import json

print("\n---------------MERGE JSON FILES----------------\n")


def merge_json(path, ip_fname, op_fname, max_size):

	os.chdir(path) 					#navigate to the directory

	i = 1
	size = 0
	result = []
	result_dict = {}

	for json_file in glob.glob(ip_fname + '*.json'):

		json_opened = open(json_file, encoding='utf-8')
		logs = json.load(json_opened)

		json_opened.seek(0,2)
		fsize = json_opened.tell()		#obtain file size

		key = list(logs)				#obtain the root key of the json file 

		if fsize <= max_size:			#check if the file is less than max_size
			if size + fsize <= max_size:
				result.extend(logs[key[0]])
			else:
				result_dict[key[0]] = result[:]
				result.extend(logs[key[0]])
				outfile = open(op_fname + str(i) +'.json', 'w')
				json.dump(result_dict, outfile, ensure_ascii=False)
				i += 1
				size = 0
				result_dict = {}
				result = []
				result.extend(logs[key[0]])
			
			size += fsize
		
		else:							#if file size is greater than max_size, file cannot be written and skipped automatically
			print("file "+ json_file + " is too large to write in a new file, try increasing the max size")

	if size <= max_size:
		result_dict[key[0]] = result[:]
		outfile = open(op_fname + str(i) +'.json', 'w')
		json.dump(result_dict, outfile, ensure_ascii=False)

#main
try: 
	path = str(input("Enter path: "))
	input_base_name = str(input("Enter input json file name suffix: "))
	output_base_name = str(input("Enter the output json file name suffix: "))
	max_size = int(input("Enter the maximum file size(in bytes): "))
	merge_json(path, input_base_name, output_base_name, max_size)
	print("Successfully merged...")

except:
	print("Error occured, try entering valid parameters...")