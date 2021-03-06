import linecache
import sys

saveStdout = sys.stdout
with open('5_re_bowtie_after.txt','w') as file:
	sys.stdout = file

	with open('4_re_bowtie.log') as f:
		zero_list = []
		row = 0
		for i,line in enumerate(f):
			line_list = line.strip('\n').split('\t')
			if line_list[-1] == '' and line_list[-2] == '0':
				zero_list.append(i)
			row += 1
	
	for i in zero_list:
		if i + 2 < row:
			next_line_list = linecache.getline('4_re_bowtie.log',i + 2).strip('\n').split('\t')
			ben_line_list = linecache.getline('4_re_bowtie.log',i+1).strip('\n').split('\t')
			if len(next_line_list[15].split(',')) >= 2:
				print (ben_line_list[0] + '\t' + ben_line_list[1] + '\t' + ben_line_list[2] + '\t' + 
						ben_line_list[3] + '\t' + ben_line_list[4] +  '\t' +  ben_line_list[5] + '\t' 
						+ ben_line_list[6] + '\t' + ben_line_list[7] + '\t' + ben_line_list[8])
			elif next_line_list[15] == '' and next_line_list[14] == '0':
				print (ben_line_list[0] + '\t'+ ben_line_list[1] + '\t'  + ben_line_list[2] + '\t' + 
						ben_line_list[3] + '\t' + ben_line_list[4] + '\t' +  ben_line_list[5] + '\t' +
						ben_line_list[6] + '\t' + ben_line_list[7] + '\t' + ben_line_list[8])
				
sys.stdout = saveStdout
sys.stdout.close()


