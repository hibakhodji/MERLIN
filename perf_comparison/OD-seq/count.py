import sys

odseq = open(sys.argv[1], 'r')
sibis = open(sys.argv[2], 'r')

TP = open("./TP.txt", "a")
FP = open("./FP.txt", "a")
FN = open("./FN.txt", "a")

temp =[]

#read OD-Seq output and store sequence names in a list
o = odseq.readlines()
for line in o:
    if ('>') in line: 
        line = line.strip()
        temp.append(line.partition(">")[2])

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
odseq.close()
TP.close()
FP.close()
FN.close()
