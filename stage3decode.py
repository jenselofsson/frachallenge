#!/usr/bin/env python3

import sys
import base64
import marshal

def rolling_xor(data, key):
    encrypted = b''
    for i, c in enumerate(data):
        encrypted += bytes((c ^ key[i % len(key)],))

    return encrypted

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " filename")
    exit()

# key grabbed from pcap
#   {"key": "AkKsFwAD"}
key = base64.b64decode("AkKsFwAD") # in bytes


datafile = open(sys.argv[1], 'rb')
data = datafile.read()
#outfile = open("out.data", 'wb')

print(type(data))
decrypted_data = rolling_xor(data, key)

#asdasdexec(marshal.loads(rolling_xor(new_payload, key)), globals(), locals())
#marshal.dump(decrypted_data,outfile)

outfile.close()
datafile.close()
