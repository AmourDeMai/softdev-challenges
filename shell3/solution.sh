#!/bin/bash
# find all the directories
dirs=`find . -type d`
# iterate every file in every directory
for dir in $dirs
do
        i="nok"
		# search all the file in the directory
        files=`find $dir -type f -atime -30`
        for file in $files
        do
                i="ok"
                #echo $file $i
        done
        if [ $i == "nok" ]; then
                #echo $dir $i
                tar -zcvf $dir.tgz $dir
				rm -r $dir
        fi
done
