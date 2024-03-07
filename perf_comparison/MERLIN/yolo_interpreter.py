from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from math import *
import sys
import pandas as pd
TOP_X_MARGIN = 54
TOP_Y_MARGIN = 24
NB_COL = 0
NB_SEQ = 0
LINE_HEIGHT = 12
LINE_WIDTH = 6
annot_d = {}
error = ['SEQ_ERROR1', 'SEQ_ERROR2', 'SEQ_ERROR3', 'SEQ_ERRORC2', 'SEQ_ERRORN1', 'SEQ_ERRORN2']


def get_info(line):
    info = {}
    info["type"] = line[0:line.find(':')]
    info["trust"] = int((line[line.find("%")-3:line.find("%")]).strip())
    info["x"] = int((line[line.find("left_x:")+7:line.find("top_y:")]).strip())
    info["y"] = int((line[line.find("top_y:")+7:line.find("width:")]).strip())
    info["width"] = int((line[line.find("width:")+6:line.find("height:")]).strip())
    return info

def yolo_pars(res_file):
    sep = ".jpg: Predicted in"
    pars, l_error, key = {}, [], ""
    f = open(res_file,'r')
    
    for line in f:
        if sep in line:
            if len(key) > 0:
                pars[key] = list(l_error)
                l_error.clear()
            key = line[0:line.find(':')]
        if "SEQ_ERR" in line:
            l_error.append(get_info(line))
    f.close()
    return pars

def pars_format(pars):
    res, res_l, res_d = {}, [], {}
 
    for file in pars.keys():
        get_grid(file)
        res_l.clear()
        for err in pars[file]:
            res_d['SEQ'] = int((err['y'] - TOP_Y_MARGIN) / LINE_HEIGHT)
            res_d['type'] = err['type']
            res_d['trust'] = err['trust']
            res_d['begin'] = ceil(((err['x'] - TOP_X_MARGIN) * NB_COL) / (NB_COL * LINE_WIDTH))
            if res_d['begin'] < 0:
                res_d['begin'] = 0
            res_d['end'] = ceil(((err['x'] - TOP_X_MARGIN) * NB_COL) / (NB_COL * LINE_WIDTH)) + ceil(err['width'] * NB_COL / (NB_COL * LINE_WIDTH))    
            res_l.insert(len(res_l), res_d.copy())
        res[file] = list(res_l)
    return res

def get_grid(pars):
    global NB_COL
    global NB_SEQ
    global annot_d
    res_d, res_l = {}, []
    name = pars.replace(".jpg", "_annot.txt")
    
    with open(name) as f:
        annot = f.readlines()
    
    NB_SEQ = int(annot[0][annot[0].find("Number of sequences : ")+21:-1].strip())
    NB_COL = int(annot[1][annot[1].find("Number of columns : ")+19:-1].strip())
    for i in range(2, len(annot)):
        t = annot[i].split()
        res_d['SEQ'] = int(t[1])
        res_d['type'] = t[2]
        res_d['begin'] = int(t[3])
        res_d['end'] = int(t[4])
        res_l.insert(len(res_l), res_d.copy())
    annot_d[name] = list(res_l)
    
def aff_pars(output): #voir pour créer un fichier PXXXXX_prediction_annot.txt pour chaque alignement analysé
    for k in output:
        name = k[0:]#k.rfind('/')+1:]
        name = name.replace(".jpg", "_yolo.txt")
        f = open(name, "w")
        for l in output[k]:
            f.write(str(l['SEQ']) + " " + l['type'] + " " + str(l['begin']) + " " + str(l['end']) + "\n")
        f.close()

def count(i, f, c):
    for i in range(0,len(f[i])):
        print(new[k][i])

#error = ['SEQ_ERROR1', 'SEQ_ERROR2', 'SEQ_ERROR3', 'SEQ_ERRORC2', 'SEQ_ERRORN1', 'SEQ_ERRORN2']
        
def count_error(f):
    global error
    e1, e2, e3, e4, e5, e6 = 0, 0 , 0 ,0 , 0, 0
    with open(f) as a:
        l = a.readlines()
    for e in l :
        t = e.split()
        e1 += (e.count(error[0]))
        e2 += (e.count(error[1]))
        e3 += (e.count(error[2]))
        e4 += (e.count(error[3]))
        e5 += (e.count(error[4]))
        e6 += (e.count(error[5]))
    return [e1, e2, e3, e4, e5, e6]

def get_metrics(new):
    global annot_d
    global error
    res = {error[0]:{'TP':0,'FP':0,'FN':0,'TN':0}, error[1]: {'TP':0,'FP':0,'FN':0,'TN':0}, error[2]:{'TP':0,'FP':0,'FN':0,'TN':0}, error[3]:{'TP':0,'FP':0,'FN':0,'TN':0}, error[4]:{'TP':0,'FP':0,'FN':0,'TN':0}, error[5]:{'TP':0,'FP':0,'FN':0,'TN':0}} 
    for k in new:
        y = k.replace(".jpg", "_yolo.txt")
        a = k.replace(".jpg", "_annot.txt")
        annot_err = (count_error(a))
        yolo_err = (count_error(y))
        for i in range(0,6):
            res[error[i]]['TP'] += min(yolo_err[i],annot_err[i])
            tmp = yolo_err[i] - annot_err[i]
            if tmp > 0:
                res[error[i]]['FP'] += tmp
            else :
                res[error[i]]['FN'] += annot_err[i] - yolo_err[i]
    for k in res:
        print(k)
        for v in res[k]:
            print(v + ' : ' + str(res[k][v]))

    prec = [round(res[error[0]]['TP']/(res[error[0]]['TP']+res[error[0]]['FP']),2) , round(res[error[1]]['TP']/(res[error[1]]['TP']+res[error[1]]['FP']),2) , round(res[error[2]]['TP']/(res[error[2]]['TP']+res[error[2]]['FP']),2), round(res[error[3]]['TP']/(res[error[3]]['TP']+res[error[3]]['FP']),2) , round(res[error[4]]['TP']/(res[error[4]]['TP']+res[error[4]]['FP']),2), round(res[error[5]]['TP']/(res[error[5]]['TP']+res[error[5]]['FP']),2)]
    rec =  [round(res[error[0]]['TP']/(res[error[0]]['TP']+res[error[0]]['FN']),2) , round(res[error[1]]['TP']/(res[error[1]]['TP']+res[error[1]]['FN']),2), round(res[error[2]]['TP']/(res[error[2]]['TP']+res[error[2]]['FN']),2), round(res[error[3]]['TP']/(res[error[3]]['TP']+res[error[3]]['FN']),2) , round(res[error[4]]['TP']/(res[error[4]]['TP']+res[error[4]]['FN']),2), round(res[error[5]]['TP']/(res[error[5]]['TP']+res[error[5]]['FN']),2)]
    f1 = [round(2*(prec[0]*rec[0])/(prec[0]+rec[0]),2) , round(2*(prec[1]*rec[1])/(prec[1]+rec[1]),2), round(2*(prec[2]*rec[2])/(prec[2]+rec[2]),2), round(2*(prec[3]*rec[3])/(prec[3]+rec[3]),2), round(2*(prec[4]*rec[4])/(prec[4]+rec[4]),2), round(2*(prec[5]*rec[5])/(prec[5]+rec[5]),2)] 

    print("precision: ")
    print(prec)
    print("recall: ")
    print(rec)
    print("f1_score: ")
    print(f1)        
        
pars = yolo_pars(sys.argv[1])
new_output = pars_format(pars)
aff_pars(new_output)
get_metrics(new_output)

