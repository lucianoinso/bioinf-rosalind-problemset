def transcribe(s):
    return s.replace("T", "U")


dna_file = open('rosalind_rna.txt', 'r')
try:
    dna_string = dna_file.readline()
    print("Original:\n" + dna_string)
    print("Transcription:\n" + transcribe(dna_string))
finally:
    dna_file.close()
