import sys

savestdout = sys.stdout
with open("4_re_bowtie.txt","w") as file:
	sys.stdout = file

	with open("3_bowtie_after.txt") as f:
		for line in f:
			line_list = line.rstrip('\n').split('\t')
			print ('>' + line_list[0] + '\t' + line_list[1] + '\t' + line_list[2] + '\t' +
				line_list[3] + '\t' + line_list[4] + '\t' + line_list[5] + '\t'  + 
				line_list[6] + '\t' + line_list[7] + '\t' + line_list[8])
			print (line_list[5])

sys.stdout = savestdout
sys.stdout.close()





