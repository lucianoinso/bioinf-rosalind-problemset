def strandGContent(seq):
    return ((seq.count("C") + seq.count("G"))/len(seq))*100


def parseFasta(filename):
    strandList = []

    f = open(filename, 'r')
    # Save the lines without the jumplines '\n'
    lines = f.read().splitlines()

    for line in lines:
        if (line[0] == '>'):
            strandList.append(line)
            lastLabel = True
        else:
            if (lastLabel):
                strandList.append(line)
                lastLabel = False
            else:
                newStrand = strandList[-1] + line
                strandList.pop()
                strandList.append(newStrand)
    return strandList


def parseFasta2(filename):
    f = open(filename, 'r')
    lines = [l.strip() for l in f.readlines()]
    
    fastaDict = {}
    fastaLabel = ""
    
    for line in lines:
        if '>' in line:
            fastaLabel = line
            fastaDict[fastaLabel] = ''
        else:
            fastaDict[fastaLabel] += line

    return fastaDict


def gcContentDict(fastaDict):
    return {key: strandGContent(value) for (key, value) in fastaDict.items()}


def highestGCContent2(resultDict):
    maxGCKey = max(resultDict, key=resultDict.get)
    return (maxGCKey, resultDict[maxGCKey])


def highestGCcontent(strandList):
    maxGc = 0
    maxStrand = ''
    strndGc = 0
    strandName = ''
    for item in strandList:
        if(item[0] == '>'):
            strandName = item[1::]
        else:
            strndGc = strandGContent(item)
        if(strndGc > maxGc):
            maxGc = strndGc
            maxStrand = strandName
    return (maxStrand, maxGc)


maxLabel, maxGC = highestGCContent2(gcContentDict((parseFasta2('rosalind_gc.txt'))))
print(f'{maxLabel[1:]}\n{maxGC}')
