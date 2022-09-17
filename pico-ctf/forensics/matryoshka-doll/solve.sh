#!/bin/sh
if [ "$#" -ne 1 ]; then
    echo "Usage $0 <url>"
    exit 1
fi

wget -q $1 -O 1_c.jpg

for i in $(seq 1 3); do
    binwalk -q -e ${i}_c.jpg

    mv _${i}_c.jpg.extracted/base_images/$(($i + 1))_c.jpg $(($i + 1))_c.jpg
done

binwalk -q -e 4_c.jpg

mv _4_c.jpg.extracted/flag.txt flag.txt

cat flag.txt

rm -rf _* *.jpg *.txt