#!/bin/bash

if [ -z "$1" ]
then
    echo "Usage: ./solve.sh <IP>"
    exit 1
fi

IP=$1

echo "$IP secrethelpdesk934752.support.futurevera.thm" | sudo tee -a /etc/hosts > /dev/null
curl -s -I http://secrethelpdesk934752.support.futurevera.thm | sed -n '4p' | grep -o 'flag{.*}'
sudo sed -i '$d' /etc/hosts
