import string 

test = "AAAAAAAAAAAATTTTTTTTTTTTT"
test = test[::-1]

with open('rosalind_revc.txt') as f:
    lines = f.readlines()

lines = lines[0][0:]

def complement(dna):
    dna = dna[::-1]
    result = ""
    for symbol in dna:
        if symbol == "A":
            result += "T"
        if symbol == "T":
            result += "A"
        if symbol == "C":
            result+="G"
        if symbol == "G":
            result += "C"
    return result
             
    
print(complement(lines))