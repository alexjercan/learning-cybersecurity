#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <IP>"
  exit 1
fi

ip=$1

mosquitto_sub -v -h "$ip" -p 1883 -t 'U4vyqNlQtf/0vozmaZyLT/15H9TF6CHg/pub' |
while IFS= read -r line; do
  echo "$line" | cut -d' ' -f2 | base64 -d | xargs -0 -I {} printf '{}\n'
done
