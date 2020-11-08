import os
from hashlib import sha256
from Crypto.Cipher import AES
from pwn import *

token = input('token: ')

def pad(msg):
    n = AES.block_size - len(msg) % AES.block_size
    return msg + bytes([n]) * n

def gen_code(code,offset):
    padded = pad(code)
    payload = padded +  sha256(padded).digest()
    return bytes.fromhex(pad(payload).hex()[2 * offset:])

io = remote('202.38.93.111','10041')
io.recv()
io.sendline(token)
io.recv()
io.sendline('1')
io.recv()

flag_text = ''
for i in range(len(flag_text),45):
    padding = ('0' * (8 + i)).encode('utf-8')
    for c in range(256):
        payload_len = int((len(flag_text) + 1)/16)
        extra = gen_code((chr(c) + flag_text).encode('utf-8'), i + 1)
        io.sendline('Alice')
        io.recv()
        io.sendline(padding.hex())
        io.recvuntil(b'say? ')
        io.sendline(extra.hex())
        raw = io.recvuntil(b'to? ')
        ans = raw[53:]
        io.sendline('Bob')
        io.recv()
        io.sendline(ans[160: 320 + payload_len * 32])
        res = io.recv()
        if 'Thanks' in res.decode('utf-8'):
            print(res)
            flag_text = chr(c) + flag_text
            print(f'now at {len(flag_text)} : {flag_text}')
            break

