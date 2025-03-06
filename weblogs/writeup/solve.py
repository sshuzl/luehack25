import base64
import urllib.parse

def decode_url_params(access_log):
    with open(access_log, "r") as f:
        # extract all bas64 strings
        links = []
        for line in f:
            links.append(line.split(' ')[6].split('=')[2])
            pass
        pass
    # convert all '%3D' to '='
    http_decoded = [urllib.parse.unquote(l) for l in links]
    # base64 decode
    clean_log = [base64.b64decode(d) for d in http_decoded]
    # print
    for log in clean_log:
        print(log.decode('ascii'))
        pass
    pass

def extract_timestamps(access_log):
    from datetime import datetime
    with open(access_log, 'r') as f:
        tss = []
        for line in f:
            ts = line.split('[')[1].split(']')[0]
            dt = datetime.strptime(ts, '%d/%b/%Y:%H:%M:%S %z')
            tss.append(dt)
        return tss

def recover_flag(access_log):
    from datetime import timedelta
    tss = extract_timestamps(access_log)
    tds = [tss[i] - tss[i-1] for i in range(1, len(tss))]
    s = list()
    for i, td in enumerate(tds):
        if i % 4 == 0:
            st = ''
        if td == timedelta(seconds=0) or ((i % 4) == 3 and td == timedelta(seconds=2)):
            st = '00' + st
        elif td == timedelta(seconds=2) or ((i % 4) == 3 and td == timedelta(seconds=4)):
            st = '01' + st
        elif td == timedelta(seconds=4):
            st = '10' + st
        elif td == timedelta(seconds=6):
            st = '11' + st
        else:
            print('Uh oh, there is something fishy!')
        if i % 4 == 3:
            s.append(chr(int(st, 2)))
        pass
    flag = ''.join(s)
    print(flag)

if __name__ == '__main__':
    import sys
    decode_url_params(sys.argv[1])
    recover_flag(sys.argv[1])
