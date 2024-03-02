for f in $1/*.xml
do 
  f="$(basename -- $f)"
  f="${f%.xml}"
  ./dataset_gen.sh $f
done
