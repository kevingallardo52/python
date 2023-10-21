"""
Program Description: This program takes a given DNA sequence 
and translates it to a protein sequence.

Author: Kevin Gallardo
Date: 10/12/23
"""

import helper

# A-U U-A C-G G-C
def transcription(dna_sequence):

    # Replace the Nucleotide Thymine (T) with Uracil (U)
    afterReplace = dna_sequence.replace("T","U")
    
    # Create the Base Pair Complement of the sequence
    # for loop to go through each letter of DNA sequence
    complement = ''
    for char in afterReplace:
        if(char == 'A'):
            complement = complement.__add__("U")
        elif(char == "U"):
             complement = complement.__add__("A")
        elif(char == "C"):
            complement = complement.__add__("G")
        elif(char == "G"):
             complement = complement.__add__("C")

    return complement

def translate(mrna):
    protein = ''
    proteinSequence = []

    # Split mrna into nucleotide triplets
    list = helper.chunk(mrna, 3)
    
    # Replace Triplets with Amino Acids
    for element in list:
        proteinSequence.append(helper.amino_acids[element])

    # Turn list into string
    protein = " ".join(list)

    return protein


dna = 'TACGCAGAAAAAAATCAGCGGGGTTGTTGGTCATTAGTCTGAATT'
# print starting DNA sequence
print("DNA Sequence")
print(dna + "\n")

# convert to mRNA and then print mRNA
mRNA = transcription(dna)
print("mRNA Sequence")
print(mRNA)
print()

# convert to Protein Sequence and print protein sequence
protein = translate(mRNA)
print("Protein Sequence")
print(protein)
