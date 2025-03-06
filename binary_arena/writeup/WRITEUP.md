# Writeup

We don't have a chance to defeat the boss since our damage is too low. However, we can change
the strength of our attack by modifying the challenge binary since it is a global variable
stored inside the binary. No complicated patching needed :)

To find the offset, we can use `objdump`, `nm` or just Ghidra which shows us the file offset conveniently.
