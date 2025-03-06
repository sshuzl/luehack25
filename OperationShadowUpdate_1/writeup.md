Extract the filesystem using `binwalk` with `binwalk -e ./path/to/bin` from the `*.bin`.

There we can a program `/etc/d3crypt0r`. This can be used to decrypt the `*.enc` firmware file.

```terminal
./d3crypt0r ./path/to/.enc decrypted_firmware_file
```

Then we extract the filesystem again and extract the flag from the filesystem.
