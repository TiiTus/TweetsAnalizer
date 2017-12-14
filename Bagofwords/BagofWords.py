i = 0
bool = 0
sP = 0
sN = 0

with open("SentiWordNet_3.0.0_20130122.txt", "r") as f:
    f1 = open("BagOfWords.txt", "w")
    for line in f.readlines():
        i = i+1
        # Traiter la ligne et ainsi de suite ...
        v = line.split('\t')
        if(bool == 0):
            f1.write("POS;ID;PosScore;NegScore;SynsetTerms \n")
            bool = 1
        else:
            content = v[0]+";"+v[1]+";"+str(int(float(v[2])*1000))+";"+str(int(float(v[3])*1000))+";"+v[4].split('#')[0]+";\n"
            print(content)
            f1.write(content)
            if int(float(v[2])*1000) == 0:
                sP = sP
            else:
                sP = sP + int(float(v[2])*1000)

            if int(float(v[3])*1000) == 0:
                sN = sN
            else:
                sN = sN + int(float(v[3])*1000)

    f1.close()
    f.close()

    print (sP)
    print (sN)