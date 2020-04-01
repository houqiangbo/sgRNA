import sys
import re
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

saveStdout = sys.stdout
with open("genome_2_sg_out.txt","w")as file:
    sys.stdout = file
    with open("genome.fa") as f:
        for line in f:
            line_list = line.strip('\n').split('\t')
            sc= [m.start() for m in re.finditer(r'CC',line_list[0].upper())]
            if len(sc) == 0:
                continue
            for index1 in sc:
                if index1 + 24 < len(line_list[0].upper()):
                    seq1 = line_list[0].upper()[index1:index1 + 23]
#                    su1 = [m.start() for m in re.finditer(r'AAAA',seq1)]
#                    su2 = [m.start() for m in re.finditer(r'TTTT',seq1)]
#                    su5 = [m.start() for m in re.finditer(r'CCCC',seq1)]
#                    su6 = [m.start() for m in re.finditer(r'GGGG',seq1)]
                    if 'AAAA' not in seq1 and 'TTTT' not in seq1 and 'CCCC' not in seq1 and 'GGGG' not in seq1:
                        print ('>' + Seq(seq1).reverse_complement() + '\n' + Seq(seq1).reverse_complement())
            sg = [m.start() for m in re.finditer(r'GG',line_list[0].upper()[::-1])]
            if len (sg) == 0:
                continue
            for index2 in sg:
                if index2 + 24 < len(line_list[0].upper()[::-1]):
                    seq2 = line_list[0].upper()[::-1][index2:index2 + 23]
#                    su3 = [m.start() for m in re.finditer(r'AAAA',seq2)]
#                    su4 = [m.start() for m in re.finditer(r'TTTT',seq2)]
#                    su7 = [m.start() for m in re.finditer(r'CCCC',seq1)]
#                    su8 = [m.start() for m in re.finditer(r'GGGG',seq1)]
                if 'AAAA' not in seq2 and 'TTTT' not in seq2 and 'CCCC' not in seq2 and 'GGGG' not in seq2:
                    print ('>' + seq2[::-1] +'\n' + seq2[::-1])		
	
sys.stdout = saveStdout
sys.stdout.close()

