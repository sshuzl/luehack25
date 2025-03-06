# Writeup - hash_guesser

## Idea

We can simply bruteforce some plaintexts until we find a valid preimage.

There are 16 bits we need to bruteforce which is doable in a fraction of a second.

## Implementation

We take the server code, adapt it slightly and test increasing numbers for the condition.

```python
import hashlib

def main():
    md5_hash = b"\x00"
    input = b""
    guess = 0
    while (not all(byte & 0x80 for byte in md5_hash)):
        input = str(guess).zfill(8).encode()
        md5_hash = hashlib.md5(input).digest()
        guess += 1
    print(f"Found solution: {input}")

if __name__ == "__main__":
    main()

# 00068800
```

Having that, we connect to the server and submit the solution.

```python
import hashlib
import pwn

def find_solution() -> bytes:
    md5_hash = b"\x00"
    input = b""
    guess = 0
    while (not all(byte & 0x80 for byte in md5_hash)):
        input = str(guess).zfill(8).encode()
        md5_hash = hashlib.md5(input).digest()
        guess += 1
    print(f"Found solution: {input}")
    return input

def main():
    io = pwn.remote('challenges.sshuzl.de', 12382)
    io.sendline(find_solution())
    io.interactive()

if __name__ == "__main__":
    main()
```
