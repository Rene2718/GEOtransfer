#!/bin/bash

for file in *.fastq
do
	input=$file
	output=`echo $input | cut -d . -f1`
	echo "Procesing "$input
	md5sum $input > "$output.txt"
	echo "Done processing" $output
done

