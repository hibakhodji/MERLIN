biolo/clustalw $1.xml -convert -output=fasta
annot_error/annot_error $1.xml > $1.txt
echo                               
aln2jpg/adoma.sh -i $1.tfa -p $1 -prot -color
wkhtmltoimage --format jpg $1.html $1.jpg
echo                               
echo "---------- Image created > 'training-data'----------"
echo                               
rm $1.fa $1.aln
mkdir temp
python3 annot_gen.py $1.jpg $1.txt ./temp/$1.xml
rm $1.txt
echo                               
python3 convert2Yolo/example.py --datasets VOC --img_path training-data/JPEGImages/ --label ./temp/ --convert_output_path training-data/Annotations/ --img_type ".jpg" --manifest_path convert2Yolo/ --cls_list_file classes.txt
echo                               
echo "---------- Error annotation YOLO file created > 'training-data/Annotations/' ----------"
echo                               
mv $1.jpg training-data/JPEGImages/
#rm $1.txt
#rm $1.xml 
rm $1.html $1.tfa 
rm logfile.txt
rm -r temp












