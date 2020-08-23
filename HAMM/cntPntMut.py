# Maybe check with reduce

def hammingDistance(s, t):
    hammingDist = 0
    for i, j in zip(s, t):
        if i != j:
            hammingDist += 1
    return hammingDist


mutatFile = open('rosalind_hamm.txt', 'r')
try:
    # [:-1] so it removes the \n from the end of the line
    s = mutatFile.readline()[:-1]
    t = mutatFile.readline()[:-1]
    hamDist = hammingDistance(s, t)
finally:
    mutatFile.close()

print(hamDist)
