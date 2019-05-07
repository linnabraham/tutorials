#!/bin/bash
# My first shell script 
# The script can be run from commandline by passing as arguments 1> path to the python file 2> input directory containing only images 3>step size for 
# rotating images 4> output directory for saving the rotated images

for i in `find ${2}*` 

do
	#echo ${i}
	python $1 $i $3 $4
done
