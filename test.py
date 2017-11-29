
TotalP = 5019455
TotalN = 6288570
TotalN=float(TotalN)
TotalP=float(TotalP)
ProbaP = float(TotalP/(TotalN+TotalP))
ProbaN = float(TotalN/(TotalN+TotalP))

print ProbaP
print ProbaN

pP=ProbaP
pN=ProbaN




with open('test.txt') as file:
    for line in file:
        mots = line.split(' ')
        #print len(mots)
        #print mots

        #pP = ProbaP
        #pN = ProbaN
        with open("Bagofwords/BagOfWords.txt") as f:
       # with open("blabla.txt") as f:
            for li in f:
                li = li.split(';')
                for mot in mots:
                    if mot.upper() == li[4].upper():
                        print mot.upper()
                        print li[4]
                        if li[2]=='0':
                            pP=pP*(1/TotalP)
                        else:
                            pP=pP*(float(li[2])/TotalP)

                        if li[3]=='0':
                            pN=pN*(1/TotalN)
                        else:
                            pN=pN*(float(li[3])/TotalN)


print pP
print pN





