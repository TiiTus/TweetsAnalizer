import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()

#Init
TotalP = 5019455 # Somme valeurs positives
TotalN = 6288570 # Somme valeurs negatives
TotalN=float(TotalN) # Cast en float
TotalP=float(TotalP) # Cast en float
ProbaP = float(TotalP/(TotalN+TotalP)) # Probabilite d'avoir un mot positif
ProbaN = float(TotalN/(TotalN+TotalP)) # Probabilite d'avoir un mot negatif

print (ProbaP)
print (ProbaN)

pP=ProbaP # Probabilite du tweet Positif
pN=ProbaN # Probabilite du tweet Negatif

tabA=[]
tabV=[]
tabN=[]
tabR=[]

rtext=""
print("")

with open("Bagofwords/BagOfWords.txt") as f:
    for li in f:
        li = li.split(';')
        if li[0] == "a":
            tabA.append(li[2]+";"+li[3]+";"+li[4])
        elif li[0] == "n":
            tabN.append(li[2] + ";" + li[3] + ";" + li[4])
        else:
            tabV.append(li[2] + ";" + li[3] + ";" + li[4])



for e in root.findall('document'):
    for f in e.findall('sentences'):
        for g in f.findall('sentence'):
            for h in g.findall('tokens'):
                for i in h.findall('token'):
                    lemma = i.find('lemma').text
                    pos = i.find('POS').text

                    if(lemma == "<fin>"):
                        #Reinit
                        print(rtext)
                        print("Positif :" +str(pP))
                        print("Negatif :" +str(pN))
                        print("")
                        rtext=""
                        pN = ProbaN
                        pP= ProbaP


                    else:

                        if pos != "NNP":

                            # Si le mot est un Nom
                            if pos[0].upper() == "N":
                                for j1 in tabN:
                                    j1 = j1.split(";")
                                    if lemma.upper() == j1[2].upper():
                                        if j1[0] == '0':
                                            pP = pP * (1 / TotalP)
                                        else:
                                            pP = pP * (float(j1[0]) / TotalP)

                                        if j1[1] == '0':
                                            pN = pN * (1 / TotalN)
                                        else:
                                           pN = pN * (float(j1[1]) / TotalN)
                                        break
                            # Si le mot est un verbe
                            elif pos[0].upper()== "V":
                                for j2 in tabV:
                                    j2 = j2.split(";")
                                    if lemma.upper() == j2[2].upper():
                                        if j2[0] == '0':
                                            pP = pP * (1 / TotalP)
                                        else:
                                            pP = pP * (float(j2[0]) / TotalP)

                                        if j2[1] == '0':
                                            pN = pN * (1 / TotalN)
                                        else:
                                            pN = pN * (float(j2[1]) / TotalN)
                                        break
                            # Sinon
                            else:
                                for j3 in tabA:
                                    j3 = j3.split(";")
                                    if lemma.upper() == j3[2].upper():
                                        if j3[0] == '0':
                                            pP = pP * (1 / TotalP)
                                        else:
                                            pP = pP * (float(j3[0]) / TotalP)

                                        if j3[1] == '0':
                                            pN = pN * (1 / TotalN)
                                        else:
                                            pN = pN * (float(j3[1]) / TotalN)
                                        break
                        rtext = rtext+ " "+lemma
