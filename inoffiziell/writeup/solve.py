import subprocess
from sage.all import GF, matrix, vector
from hashlib import sha256
from Crypto.Cipher import AES

CAPTURE_FILE = 'surveillance.pcapng'
p = 340282366920938463463374607431768211297

def get_pcap_data(file: str) -> str:
    cmd = ['tshark', '-r', file, '-Tfields', '-Y', 'data', '-e', 'data']
    print(' '.join(cmd))
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    raw_data = p.communicate()[0].decode('ascii')
    return bytes.fromhex(raw_data).strip().decode('ascii')

def parse_data(file: str) -> tuple[list[list[int]], list[int], bytes]:
    def parse_challenge(data: bytes) -> list[int]:
        return list(map(int, data.strip().split(' ')))
    def parse_response(data: bytes) -> int:
        return int(data.strip())
    def parse_enc_flag(data: bytes) -> bytes:
        return bytes.fromhex(data)
    
    challenges = list()
    responses = list()
    enc_flag = None
    data = get_pcap_data(file).split('\n')
    assert len(data) % 4 == 0

    for i in range(0, len(data), 4):
        if data[i+2] != 'ACCESS GRANTED':
            print("Warn: Skipped data!")
            continue

        challenge = parse_challenge(data[i])
        response = parse_response(data[i+1])
        enc_flag = parse_enc_flag(data[i+3])

        challenges.append(challenge)
        responses.append(response)
        pass

    return challenges, responses, enc_flag

def decrypt_flag(enc_flag: bytes, key: list[int]) -> bytes:
    aes_iv = b'\0'*16
    aes_key = sha256(' '.join(map(str, key)).encode('utf-8')).digest()
    aes = AES.new(aes_key, AES.MODE_CFB, aes_iv)
    return aes.decrypt(enc_flag)

def main():
    AA, bb, enc_flag = parse_data(CAPTURE_FILE)

    assert len(AA) == 40
    assert len(bb) == 40
    
    AA = matrix(GF(p), 40, AA)
    bb = vector(GF(p), bb)
    key = list(AA.solve_right(bb))

    print(decrypt_flag(enc_flag, key))
    return

if __name__ == '__main__':
    main()
    pass
