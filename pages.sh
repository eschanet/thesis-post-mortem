#!/bin/bash

firstday=0

for day in {100..0..-1}; do
    git checkout $(git rev-list -n 1 --before="$day days ago" master)
    # org-mode SLOC
    pdftotext thesis.pdf
    lines=$(wc -l thesis.txt)
    if [ $? -eq 0 ]; then
        lines=$(echo $lines | cut -d ' ' -f 1)
        #echo x | make
        if [ $? -eq 0 ]; then
            if [ $firstday -eq 0 ]; then
                firstday=$day
            fi
            currentday=$(expr $firstday - $day)
            if [ $currentday -ge 100 ]; then
                break
            fi
            # number of pdf pages
            pages=$(pdfinfo thesis.pdf | grep 'Pages:' | rev | cut -d ' ' -f 1 | rev)
            echo -n $currentday, >> data-days
            echo -n $lines, >> data-sloc
            echo -n $pages, >> data-pages
        fi
    fi
done
