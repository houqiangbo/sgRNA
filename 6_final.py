import linecache
import sys
import os
import random

f = open('final.txt','w')

text = open('bowtie_after.txt').readlines()
count = len(text)

start_line = linecache.getline('bowtie_after.txt',1)
start_line_list = start_line.rstrip('\n').split('\t')

diff_list = [] 
for i in range(2,count + 1):
	
	next_line = linecache.getline('bowtie_after.txt',i)
	next_line_list = next_line.rstrip('\n').split('\t')
	
	if start_line_list[0] != next_line_list[0]:
		diff_list.append(i)
		
		start_line_list = next_line_list

diff_list.insert(0,1)
diff_list.append(count)

for i in range(len(diff_list) - 1):
	dict_m = {}
	dict_p = {}
	for elem in (text[diff_list[i] - 1:diff_list[i + 1] - 1]):
		if elem.strip('\n').split('\t')[4] == '-':
			dict_m.update({elem.rstrip('\n').split('\t')[-1]:elem.rstrip('\n').split('\t')})
		else:
			dict_p.update({elem.rstrip('\n').split('\t')[-1]:elem.rstrip('\n').split('\t')})

	sort_dict_m = sorted(dict_m.items(),key=lambda dict_m:dict_m[0])[::-1]
	sort_dict_p = sorted(dict_p.items(),key=lambda dict_p:dict_p[0])

	total_list = sort_dict_p + sort_dict_m
    
	for seq in random.sample(total_list, 6):
		f.write(' '.join(seq[1]) + '\n')
    #print(total_list)	
	





















