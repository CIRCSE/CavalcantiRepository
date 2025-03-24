

import io


# questo script decompone il trattato d'amore e genera n file contententi solo il testo di ogni poemetto

titleList= []

with open('trattato_title_list.txt', 'r') as file: 
    for line in file:
        titleList.append(line.strip())


allText = {}
currentKeyFile = ""
currentFileContent = ""
tilePositionIdx = 0
title_fullTitleMapping = {}
with open('trattato.txt', 'r') as file:
    for line in file:
        if len(line.strip()) <= 8 and len(line.strip()) != 0:
            currentKeyFile = line.strip()
            currentFileContent = ""
            allText[currentKeyFile] = ""
            title_fullTitleMapping[currentKeyFile] = titleList[tilePositionIdx]
            tilePositionIdx += 1
        else:
            allText[currentKeyFile] +=  line.strip()+"\n"


for key in allText:
    
    with io.open("trattatoFiles/"+title_fullTitleMapping[key]+".txt",'w',encoding='utf8') as f:
        f.write(allText[key].strip())
        f.close()
    
print("done")