1 - /biolo/clustalw $1.xml -convert -output=fasta --> converts an XML alignement to FASTA.

2 - annot_error/annot_error $1.xml > $1.txt --> generates SIBIS error annotations (txt files, these are later used to create YOLO annotations which are necessary for training)

3 - /aln2jpg/adoma.sh -i $1.tfa -p $1 -prot -color --> converts FASTA to HTML.

4 - wkhtmltoimage --format jpg $1.html $1.jpg --> converts HTML to JPEG.

5 - annot_gen.py $1.jpg $1.txt ./temp/$1.xml --> produces annotations in PASCAL VOC format. (This step makes it easier to create YOLO annotations using the txt files that we generated using annot_error: annotating objects in images is usually handled manually using a labelling tool. In this case, however, it is difficult given the number of errors in a single alignment. Since we already have txt annotation files we decided to automatically generate our YOLO annotations, and this is where PASCAL VOC comes in. Unlike YOLO format, PASCAL VOC is simple to read and understand.)

6 - python3 convert2Yolo/example.py ... --> converts PASCAL VOC format to YOLO format.

NOTES: 

* The generated YOLO annotations (bounding boxes) can be checked using https://github.com/ivder/YoloBBoxChecker
* Training, validation, and test data can be found in ../darknet/data/train.txt, ../darknet/data/valid.txt, and ../darknet/data/test.txt, and retrieved from https://zenodo.org/records/6637475#.ZCV9ai0RppQ
* You might wanna replace nawk with awk in aln2jpg/convert_aln.py
