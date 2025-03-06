# Writeup

## TL;DR

The **invest** option allows for an integer overflow. Since it does not take into account
the current size of the integer. Investing once, then eating something, then repeatedly
investing will lead to a negative balance.

## Explanation

To get the flag, we need a negative balance. However we cannot achieve this in a straightforward way
since we can only buy food until the balance reached 0. And the invest option only multiplies the balance with 4.

At first glance, there is no apparent way to reach a negative balance since we are starting out with 1$.

However, the program is vulnerable to an **Integer Overflow**.

In C integers have a fixed length. The integer used in this challenge is a 32 bit signed integer.
Signed integers are commonly represented in the Two's complement in which the first bit is the sign bit,
which represents whether the number is negative or positive.

Multiplying our balance by 4 is equivalent to shifting the binary representation of the number 2 position to the left.

If we shift a lot of times, we will end up shifting the bits over the limit of 32 bits, which will drop them.

The idea to solve this challenge is that we want to shift the number that often to the left such that the first bit,
which is the sign bit, will be 1.

However, since the **invest** option multiplies by 4, which shifts by 2 positions, we will shift the 1 over the
first position. Consider the following as a visualization:

```
# Example for 8 bits

00000001
# Invest
00000100
# Invest
00010000
# Invest
01000000
# Invest
00000000 # 1 is shifted beyond the end!
```

Using that, we can't set the first bit to one.

However, we have a second option **eat**. Using eat, we can decrement our balance by 1.
The idea is, that we first **invest** once, to get balance 4 (binary 100) and then **eat**
to get balance 3 (binary 011). If we then **invest** multiple times, we set the first bit.

Consider the following as a visualization for integer with 8 bits:

```
# Initial balance
00000001 (1)
# Invest
00000100 (4)
# Eat
00000011 (3)
# Invest
00001100 (12)
# Invest
00110000 (48)
# Invest
11000000 (-64)
```

The same logic applies to integers with size 32 bits.

## Solve script

```python
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

io.interactive() # keep connection open and display the received data
```
