import csv
# Read Keywords and pairs
# Uses a csv File from 
wordlist = [] # init dictionary
language = [] # In case naming changes
with open('wordsTochange.csv', mode='r') as infile:
    reader = csv.reader(infile,delimiter=';')
    line_count = 0
    for i,rows in enumerate(reader): 
        if i == 0:
            for columns in rows:
                
                language.append(columns)
            continue
        else:
            wordlist.append((rows[0],rows[1])) # create word pair touple
 
#For testing            
if __name__ == "__main__":
    print("available language",language)
    print("Wordlist")
    print(wordlist)