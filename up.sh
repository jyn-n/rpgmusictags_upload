#!/bin/sh

ul_file=$(mktemp)

python up.py $1 > $ul_file

[[ 0 -eq $? ]] && curl "rpgmusictags.org/Upload?format=jsv" -d @$ul_file

rm $ul_file

