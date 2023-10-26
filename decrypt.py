#!/usr/bin/env python3

import base64
import sys

def rolling_xor(data, key):
    encrypted = b''
    for i, c in enumerate(data):
        encrypted += bytes((c ^ key[i % len(key)],))

    return encrypted

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " data")
    exit()

# Key encoded as
# >>> key = uuid.getnode().to_bytes(length=6, byteorder='big')
# b'ZK\x1d\xfe&\x8a'
# >>> base64.b64encode(key)
# b'Wksd/iaK'
# >>> base64.b64encode(key).decode()
# 'Wksd/iaK'

# key grabbed from pcap
#   {"key": "AkKsFwAD"}
key = base64.b64decode("AkKsFwAD") # in bytes
#data = base64.b64decode("eWDPeG1uYyzINTojIDHAcmVzID8=") # in bytes
data = sys.argv[1]

decrypted = rolling_xor(base64.b64decode(data), key)

print(decrypted.decode())
