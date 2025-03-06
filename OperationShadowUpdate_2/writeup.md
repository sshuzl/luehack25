# Writeup

Dropping the binary into Ghidra, we can find that the stored key is first XOR'd with \xAA
and then XORed onto the firmware image.

To obtain the key, we can copy it from the binary file and XOR it with \xAA ourselves.

Otherwise we can use that it is a simple XOR "encryption" and "decrypt" a big file just containing zeros.
This will directly give us the key.

```terminal
+Create test file
dd if=/dev/zero of=f.bin bs=1 count=7776000

+Use decryptor to encrypt f.bin
./d3cryptor f.bin f.enc

+Inspect file at 0x160000
```
