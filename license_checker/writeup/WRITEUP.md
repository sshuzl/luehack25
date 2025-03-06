# license_checker - Writeup

 When inspecting the given binary with ghidra, you'll find that the input is scrambled, xord and put through a loopkup-table before it is compared against a hard-coded byte sequence. The goal seems to be to find the valid input, that matches the hard-coded sequence, when put through the functions.


## Solve
1. Find that the input is shifted by a fixed number: `(i + 23) % INPUT_LENGTH`
2. Find that the input is then xor with a constant derived from `i`: `(1337 * i) % 256`
3. Find that the input is then substituted using a lookuptable.
4. Extract the lookup-table, xored values and then use the encrypted-data, the input is compared against to invert the previous 3 steps to obtain the input, that leads to the encrypted-data.
5. Should reveal that you need to input the flag.

In the `solve.py` you can insert the lookup-table and hard-coded byte sequence to compute the correct input. 