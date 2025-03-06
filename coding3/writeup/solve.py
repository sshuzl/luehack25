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
        msg = [int(x) for x in receive('').split(' ')]
        first, second = max(msg), min(msg)
        if abs(first) < abs(second):
            first, second = second, first
        send(' '.join([str(first), str(second)]))
        pass
    print('Flag:', receive(''), file=sys.stderr)
    pass
