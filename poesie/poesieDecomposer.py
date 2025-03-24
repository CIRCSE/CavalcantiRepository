

import io


# questo script decompone le poesie e genera n file contententi solo il testo di ogni poesia



allText = {}
currentKeyFile = ""
currentFileContent = ""
tilePositionIdx = 0
title_fullTitleMapping = {}
nextIsTitle = False
with open('Poesie_Cavalcanti.txt', 'r') as file:
    for line in file:
        if line.strip().lower().startswith("poesia numero") :
            currentKeyFile = line.strip().lower().replace("poesia numero","").strip() + " - "
            currentFileContent = ""
            nextIsTitle = True
        elif nextIsTitle and len(line.strip()) > 0:
            currentKeyFile += line.strip()
            allText[currentKeyFile] = ""
            currentFileContent = ""
            nextIsTitle = False
        elif nextIsTitle is False:
            allText[currentKeyFile] +=  line.strip()+"\n"


for key in allText:
    
    with io.open("poesieFiles/"+key+".txt",'w',encoding='utf8') as f:
        f.write(allText[key].strip())
        f.close()
    
print("done")