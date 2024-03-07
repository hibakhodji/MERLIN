

def stats(yolof, sibisf):

    yolo = open(yolof, 'r')
    sibis = open(sibisf, 'r')


    TP = open("TP.txt", "a")
    FP = open("FP.txt", "a")
    FN = open("FN.txt", "a")

    temp =[]

    #read yolo output and store sequence number in a list
    y = yolo.readlines()
    for line in y:
        temp.append(line.split()[0])
    temp = list(dict.fromkeys(temp))



    sb =[]
    with open(sibisf, 'r') as sibis:
        for line in sibis.readlines()[2:]:
            sb.append(line.split()[1]) 
        sb = list(dict.fromkeys(sb))


    #save TP and FP   
    for e in temp:
        if e in sb: 
            TP.write(e + '\n')
        else: FP.write(e + '\n')


    for seq in sb:
        if seq not in temp: FN.write(seq + '\n')        


    yolo.close()
    sibis.close()            
    TP.close()
    FP.close()
    FN.close()



from pathlib import Path
import os

# file containing sequence names
seq = open("data.txt",'r')
s = seq.read().split() 

directory = "test_annot_v7"

files = Path(directory).glob('*')
for line in s:
    yolo_filename = os.path.basename(line+"_yolo.txt")
    sibis_filename = os.path.basename(line+".txt")
    stats(os.path.join(directory, yolo_filename), os.path.join(directory, sibis_filename))
   

