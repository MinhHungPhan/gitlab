#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import time
import struct
import hashlib
import binascii

trans_5C = ''
trans_36 = ''
for x in xrange(256):
    trans_5C += chr(x ^ 0x5C)
    trans_36 += chr(x ^ 0x36)

# https://tools.ietf.org/html/rfc3548.html#page-6
b32_lookup = {
    '3': 27L, '2': 26L, '5': 29L, '4': 28L, '7': 31L, '6': 30L, 'A': 0L,
    'C': 2L, 'B': 1L, 'E': 4L, 'D': 3L, 'G': 6L, 'F': 5L, 'I': 8L, 'H': 7L,
    'K': 10L, 'J': 9L, 'M': 12L, 'L': 11L, 'O': 14L, 'N': 13L, 'Q': 16L,
    'P': 15L, 'S': 18L, 'R': 17L, 'U': 20L, 'T': 19L, 'W': 22L, 'V': 21L,
    'Y': 24L, 'X': 23L, 'Z': 25L
}


def hmac(key, msg):
    # https://www.ietf.org/rfc/rfc2104.txt - sha1, 64 block
    outer = hashlib.sha1()
    inner = hashlib.sha1()
    if len(key) > 64:
        key = hashlib.sha1(key).digest()
    key = key + chr(0) * (64 - len(key))
    outer.update(key.translate(trans_5C))
    inner.update(key.translate(trans_36))
    inner.update(msg)
    outer.update(inner.digest())
    return outer.digest()


def base32_decode(msg):
    # https://tools.ietf.org/html/rfc3548.html - base32 nopadding
    quanta, leftover = divmod(len(msg), 8)
    if leftover:
        raise TypeError('only no-padded b32 accepted')
    parts = []
    acc = 0
    shift = 35
    try:
        for c in msg:
            acc += b32_lookup[c] << shift
            shift -= 5
            if shift < 0:
                # http://opensource.apple.com//source/python/python-3/python/Modules/binascii.c
                parts.append(binascii.unhexlify('%010x' % acc))
                acc = 0
                shift = 35
    except:
        raise TypeError('non b32 character')
    return ''.join(parts)


def generate_otp(key, hotp_value=None):
    try:
        # convert HOTP to bytes
        # https://tools.ietf.org/rfc/rfc6238.txt
        # http://opensource.apple.com//source/python/python-3/python/Modules/structmodule.c
        hotp_value = struct.pack('>q', hotp_value or int(time.time() / 30))
        # convert base32 key to bytes
        key = base32_decode(key.upper())
        # generate HMAC-SHA1 from HOTP based on key
        HMAC = hmac(key, hotp_value)
        # compute hash truncation
        cut = ord(HMAC[-1]) & 0x0F
        # encode into smaller number of digits
        return '%06d' % (
            (struct.unpack('>L', HMAC[cut:cut + 4])[0] & 0x7FFFFFFF) % 1000000
        )
    except Exception:
        return None


if not len(sys.argv) == 2:
    print('provide sercret key and secret key only as arg')
    sys.exit(1)

otp = generate_otp(sys.argv[1])

if not otp:
    print('OTP already generated')
    sys.exit(0)
else:
    print(otp)
    sys.exit(0)
