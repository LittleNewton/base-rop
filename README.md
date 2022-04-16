# ROP 利用

有些不错的 exp，在 kali linux + pwntools 环境下运行成功。

Note. ret2libc3 需要与本机的 libc.so 版本一致，否则 exp 不起作用。

## 经过修改的 ret2shellcode

CTF-wiki.org 网站上的 ret2shellcode 是有问题的，其 bss 段没有可执行权限。

经用 010editor 对该 elf 文件的 `struct program_header_table` 的 `[3]` 号 loadable 条目进行权限修改，得到 `src/ret2shellcode` elf 文件。有问题的原文件是 `src/ret2shellcode_NX`

