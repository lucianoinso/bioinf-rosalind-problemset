def count_nuc_freq(s):
    a = c = g = t = 0
    for nucl in s:
        if(nucl == 'A'):
            a = a + 1
        elif(nucl == 'C'):
            c = c + 1
        elif(nucl == 'G'):
            g = g + 1
        elif(nucl == 'T'):
            t = t + 1

    return {"A": a, "C": c, "G": g, "T": t}


def count_nuc_freq2(s):
    freq_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in s:
        freq_dict[nuc] += 1
    return freq_dict


dna_file = open('rosalind_dna.txt', 'r')
try:
    dna_string = dna_file.readline()[:-1]
    print(count_nuc_freq(dna_string))
finally:
    dna_file.close()
