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
