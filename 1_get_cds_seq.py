import re,sys,os
import logging
from Bio.SeqIO import parse
from Bio.Seq import Seq,translate
from Bio.SeqIO import parse

seqs = {}
fid = open('pig_lncRNA.fa','w')

for ret in parse('/home/db/genomes/pig/GCF_000003025.6_Sscrofa11.1_genomic.fna','fasta'):
    seqs[ret.id] = str(ret.seq)

seq_s = set()  
gene_id = {} 

for rem in open('lnc_RNA.gff').readlines():
    if rem[0] != '#':
        allinf = re.split('\t',rem)

        if allinf[2] == 'lnc_RNA':
            if len(re.findall('gene=(.+?);',allinf[8])) != 0:
                geneid = re.findall('gene=(.+?);',allinf[8])[0]
		
                if geneid not in gene_id.keys():
                    gene_id[geneid] = 1
                    st1 = int(allinf[3]) - 1
                    st2 = int(allinf[4])
                    if allinf[6] == "-":
                        fid.write(geneid + '\t' + str(gene_id[geneid]) + '\t'+ allinf[3] +  '\t'+
									 allinf[4] + '\t'+ allinf[6] + '\t' + str(Seq(seqs[allinf[0]][st1:st2]).reverse_complement()) + '\n')
                    else:
                        fid.write(geneid + '\t' + str(gene_id[geneid]) + '\t'+ allinf[3] +  '\t' + allinf[4] + '\t'+ 
									allinf[6] + '\t' + seqs[allinf[0]][st1:st2] + '\n')
                else:
                    gene_id[geneid] += 1
                    st1 = int(allinf[3]) - 1
                    st2 = int(allinf[4])
                    if allinf[6] == "-":
                        fid.write(geneid + '\t' + str(gene_id[geneid]) + '\t'+ allinf[3] +  '\t'+ allinf[4] + '\t'+ 
								allinf[6] + '\t' + str(Seq(seqs[allinf[0]][st1:st2]).reverse_complement()) + '\n')
                    else:
                        fid.write(geneid + '\t' + str(gene_id[geneid]) + '\t'+ allinf[3] +  '\t' + allinf[4] + '\t'+ 
								allinf[6] + '\t' + seqs[allinf[0]][st1:st2] + '\n')

fid.close()

                    
