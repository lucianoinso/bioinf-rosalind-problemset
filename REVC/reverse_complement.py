def reverseComplement1(seq):
    dnaRevComp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    result = ''
    for nucl in seq:
        result = result + (dnaRevComp[nucl])
    return result[::-1]


def reverseComplement2(seq):
    dnaReverseComplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return (''.join([dnaReverseComplement[nucl] for nucl in seq])[::-1])


def reverseComplement3(seq):
    mapping = str.maketrans("ACGT", "TGCA")
    return seq.translate(mapping)[::-1]


print(reverseComplement1("ACGTGCAGTACA"))
print(reverseComplement2("ACGTGCAGTACA"))
print(reverseComplement3("ACGTGCAGTACA"))
