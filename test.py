"""
このファイルに解答コードを書いてください
"""

#Read the file and get its size
lines = open("input.txt", "r")
lines = lines.read().split('\n')
size = len(lines)

#Get the number m
number_m = int(lines[-2])

#initialize help variables
lines_dict = {}
numbers_list = []
count = 0

#loop through the pairs i:s
for i in range(size - 2):
	#get number i and string s
	line_number, line_word = lines[i].split(":")
	line_number = int(line_number)
	
	#add i and s to a dictionary
	lines_dict[line_number] = line_word

	#if m is a multiple of i, add i to a list
	if number_m % line_number == 0:
		count += 1
		numbers_list.append(line_number)

#sort the multiple list
numbers_list.sort()

#loop through the sorted list and get the corresponding s string from dict
out_str = ""
for  number in numbers_list:
	out_str += lines_dict[number]

#print output
if count > 0:
	print(out_str)
else:
	print(number_m)