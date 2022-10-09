from keywords import wordlist,language    
from fileselectionGui import fileName,fileEnding

# Makes new File with words from keywords of colummn 2 replaced with keywords of colummn 1
# Uses Keywords and pairs
#setup
fromLanguage = 1
toLanguage   = 2
#end setup
readfile = ""
with open((fileName+fileEnding),'r', encoding="utf8") as infile:
    readfile = infile.readlines()

modFile = []
#Use shortest doubl loop
if len(wordlist) > len(readfile):
    for word in wordlist:
        for line in readfile:
            modFile.append(line.replace(word[fromLanguage],word[toLanguage]) ) 
else:
    for line in readfile:
        for word in wordlist:
            modFile.append(line.replace(word[fromLanguage],word[toLanguage]) ) 

with open((fileName+language[toLanguage]+fileEnding),'w', encoding="utf8") as outfile:
    outfile.wirte(modFile)  