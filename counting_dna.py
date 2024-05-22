
input_str = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"


with open('rosalind_dna.txt') as f:
    lines = f.readlines()

lines = lines[0][0:]

def occurences(dna):
    output = []
    output.append(dna.count('A'))
    output.append(dna.count('C')) 
    output.append(dna.count('G'))
    output.append(dna.count('T'))
   
    return output 

    

print(occurences(lines))
