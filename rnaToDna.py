test_str = "GATGGAACTTGACTACGTAAATT"



with open('rosalind_rna.txt') as f:
    lines = f.readlines()

lines = lines[0][0:]


def dnaToRna(dna):
    return  dna.replace("T","U")
    

print(dnaToRna(lines))