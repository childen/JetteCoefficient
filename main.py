import sys

name1 = sys.argv[1]
name2 = sys.argv[2]

def countLetters(str):
    counts = list()
    str = str.lower()
    str = str.replace(" " , "")
    seen = list()
    for letter in list(str):
        if letter not in seen:
            seen.append(letter)
            print(seen)
            counts.append(str.count(letter))
    return counts

def calcJetteCoefficient(counts, subcounts):
    if len(counts) > 1:
        sum = counts[0] + counts[-1]
        if sum > 9:
            subcounts.append(int(sum/10))
            subcounts.append(sum % 10)
        else:
            subcounts.append(sum)
        return calcJetteCoefficient(counts[1:-1], subcounts)
    elif len(counts) == 1:
        subcounts.append(counts[0])
    if len(subcounts) == 2:
        return subcountsa
    return calcJetteCoefficient(subcounts, list())


print(calcJetteCoefficient(countLetters(name1+name2), list()))
