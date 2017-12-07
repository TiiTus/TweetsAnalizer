import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()

for e in root.findall('document'):
    for f in e.findall('sentences'):
        for g in f.findall('sentence'):
            for h in g.findall('tokens'):
                for i in h.findall('token'):
                    lemma = i.find('lemma').text
                    pos = i.find('POS').text
                    print(lemma,pos)

