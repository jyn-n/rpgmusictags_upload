#!/bin/sh

ul_file=$(mktemp)

#python up.py $1 > $ul_file

python ul_mid.py $1 | while read l; do
	python ul_head.py $2 > $ul_file
	echo $l >> $ul_file
	python ul_tail.py >> $ul_file
	[[ 0 -eq $? ]] && curl "rpgmusictags.org/Upload?format=jsv" -d @$ul_file
	#cat $ul_file
	#break
done

rm $ul_file

