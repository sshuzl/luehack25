import sys

DEBUG=True

def send(msg):
    print(msg, file=sys.stdout)
    if DEBUG:
        print(msg, file=sys.stderr)

def receive(msg):
    if DEBUG:
        print(msg, file=sys.stderr, end='', flush=True)
    ret = input(msg)
    if DEBUG:
        print(ret, file=sys.stderr)
    return ret

if __name__ == '__main__':
    for _ in range(100):
        a, b = [int(x) for x in receive('').split(' ')]
        send(a % b)
        pass
    print('Flag:', receive(''), file=sys.stderr)
    pass
