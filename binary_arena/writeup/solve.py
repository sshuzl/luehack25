import pwn

# extracted after first connection

serial_number = 4777618179743051134
io = pwn.remote("challenges.sshuzl.de", 12380)

# serial_number = 1337
# io = pwn.process("../bin/PINpoint")

cross_sum = 0
tmp = serial_number
while (tmp > 0):
    cross_sum += tmp % 10
    tmp //= 10

pin = ((cross_sum * 8) + 40) << 2

io.sendline(str(pin).encode())

# leave connection open
io.interactive()
