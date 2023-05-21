#!/bin/bash

if [ $# -lt 2 ]; then
  echo "Usage: $0 <ip> <cmd> [arg]"
  exit 1
fi

ip=$1

if [ $# -gt 2 ]; then
    arg="$(shift 2; echo "$*")"

    json='{"id": "cdd1b1c0-1c40-4b0f-8e22-61b357548b7d", "cmd": "'"${2}"'", "arg": "'"${arg}"'"}'
else
    json='{"id": "cdd1b1c0-1c40-4b0f-8e22-61b357548b7d", "cmd": "'"${2}"'"}'
fi

echo -n $json | base64 -w 0 | xargs -0 mosquitto_pub -h $ip -t "XD2rfR9Bez/GqMpRSEobh/TvLQehMg0E/sub" -m
