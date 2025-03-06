import pwn
from sage.all import kronecker

# Secure group from RFC 3526
prime = int("""
FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1
29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD
EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245
E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED
EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D
C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F
83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D
670C354E 4ABC9804 F1746C08 CA18217C 32905E46 2E36CE3B
E39E772C 180E8603 9B2783A2 EC07A28F B5C55DF0 6F4C52C9
DE2BCBF6 95581718 3995497C EA956AE5 15D22618 98FA0510
15728E5A 8AACAA68 FFFFFFFF FFFFFFFF""".replace('\n', '').replace(' ', ''), 
16)

HOST = 'challenges.sshuzl.de'
PORT = 12381

def receive_commitment(conn: pwn.remote) -> tuple[int, int, int]:
  conn.recvuntil(b'Commitment: ')
  return tuple(map(int, conn.readline().strip().split(b', ')))

def send_guess(conn: pwn.remote, guess: bool) -> None:
  conn.recvuntil(b'> ')
  conn.sendline(str(int(guess)).encode('ascii'))
  return

def receive_proof(conn: pwn.remote) -> tuple[bool, int, int]:
  correct = b'Correct!' in conn.recvuntil(b'Proof: ')
  a, b = tuple(map(int, conn.recvline().strip().split(b', ')))
  return correct, a, b

def receive_balance(conn: pwn.remote) -> int:
  conn.recvuntil(b'balance is ')
  return int(conn.recvline().strip().split(b' ')[0])

def receive_flag(conn: pwn.remote) -> str:
  # conn.recvline()
  return conn.recvline().decode('ascii')

def get_guess(A, B, C) -> bool:
  return kronecker(A, prime) * kronecker(B, prime) != kronecker(C, prime)

def play(conn: pwn.remote, progress):
  balance = receive_balance(conn)
  progress.status(f"{balance} €")
  while True:
    A, B, C = receive_commitment(conn)
    send_guess(conn, get_guess(A, B, C))
    proof = receive_proof(conn)
    if proof[0] and balance == 199:
      progress.success(f"Won!")
      pwn.log.info(f"Flag: {receive_flag(conn)}")
      return
    balance = receive_balance(conn)
    progress.status(f"{balance} €")
    pass
  return

def main():
    pwn.context.log_level = 'info'
    conn = pwn.remote(HOST, PORT)
    progress = pwn.log.progress(f"Playing")
    play(conn, progress)
    conn.close()
    return

if __name__ == '__main__':
  main()
  pass
