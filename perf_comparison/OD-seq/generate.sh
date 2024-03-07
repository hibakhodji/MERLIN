biolo/clustalw $1.xml -convert -output=fasta
OD-seq -i $1.tfa  -o $1
python3 count.py $1 $1.txt
rm $1.tfa
#rm $1
