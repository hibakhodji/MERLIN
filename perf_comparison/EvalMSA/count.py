import re
import sys


evalmsa = open(sys.argv[1], 'r')
sibis = open(sys.argv[2], 'r')

TP = open("./TP.txt", "a")
FP = open("./FP.txt", "a")
FN = open("./FN.txt", "a")

temp =[]


#read evalmsa output and store sequence names in a list
ev = evalmsa.readlines()
for line in ev:
    if ('Outliers') in line and len(line.split())> 1: 
        empty = False
    elif ('Outliers') in line and len(line.split())<= 1:
        empty = True


if (empty==False):        
    for line in ev:
        if ('Outliers') in line:
            line= re.sub(r"\([^()]*\)", "", line.split()[1])
            temp.append(line)
        elif ('(') in line:
            line= re.sub(r"\([^()]*\)", "", line.split()[0])
            temp.append(line)

temp = list(dict.fromkeys(temp))

print(temp)

#read sibis error annotation file            
sb =[]
with open(sys.argv[2], 'r') as sibis:
    for line in sibis.readlines()[2:]:
        sb.append(line.split()[0]) 
    sb = list(dict.fromkeys(sb))

print(sb)
#save TP and FP   
for line in temp:
    if line in sb: 
        TP.write(line + '\n')
    else: FP.write(line + '\n')

#save FN   
for seq in sb:
    if seq not in temp: FN.write(seq + '\n')  
        

sibis.close()     
evalmsa.close()
TP.close()
FP.close()
FN.close()
