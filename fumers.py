import mcb185 as mcb
import sys
import itertools

filename = sys.argv[1]
for name, seq in mcb.read_fasta(filename):
	print(len(seq))
	for k in range(2, 100):
		#print(k)
		seen = {}
		for i in range(0, len(seq)-k+1):
			kmer = seq[i:i+k]
			seen[kmer] = True
		if len(seen.keys()) < 4**k:
			print(k, 4**k, len(seen.keys())) #what number of kemers that exist/dont
			break
		#print(len(seen.keys()), 4**k)
		
# kmers that dont exist...
for ktup in itertools.product("ACGT", repeat=4):
	kmer = ''.join(ktup)
	print(kmer)
	# compare to seen, print not seen ones
