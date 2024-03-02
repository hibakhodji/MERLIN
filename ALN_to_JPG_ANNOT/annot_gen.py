from pascal_voc_writer import Writer
import cv2
import sys


path_image=sys.argv[1]
path_file=sys.argv[2]
path_output=sys.argv[3]

image = cv2.imread(path_image)
h, w, c = image.shape
writer = Writer(path_image, w, h)
f = open(path_file,"r") 
#columns=len(f.readline().split())
lines = f.readlines()[2:]
fontheight=12
fontwidth=6
leftborder=68 #50
topborder=27 #25


for line in lines:
    #name
    name=line.split(' ')[2]
    #sequence_number
    sq=int(line.split(' ')[1])
    xmin=leftborder + (fontwidth * int(line.split(' ')[3]))
    xmax=leftborder + (fontwidth * int(line.split(' ')[4]))
    ymin=topborder + (fontheight * sq)
    ymax=ymin + fontheight
    writer.addObject(name, xmin, ymin, xmax, ymax)
    writer.save(path_output)















