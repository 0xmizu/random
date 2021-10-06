# start bin on remote vm and debug on local

from pwn import *
from subprocess import Popen

context.arch = "amd64"
context.terminal = "kitty"

payload = b"some payload"

s = ssh(
    host="localhost",
    port=2222,
    user="user",
    password="user"
)

p = s.process(
    ["gdbserver","localhost:1111",
     "/opt/phoenix/amd64/stack-six"]
)

# contents of dbg_connect
# gdb -ex "target remote localhost:1111"
proc = Popen(
    "kitty --class debugger -e dbg_connect",
    shell=True,
    stdin=None,
    stdout=None,
    stderr=None,
    close_fds=True)

p.interactive()
