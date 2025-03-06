The cheat code table is inside the binary and can be viewed with `strings ./pacman`.

The challenge can be solved by using the cheat code `"UP-DOWN-X-X-Y-B-A-LR-RIGHT"` which prints the flag.

**Note:**

After the contest we noticed that the uploaded challenge binary `pacman` was built with the musl standard C libary
whereas common linux distributions only have glibc standard C library preinstalled.

Due to that, you might run into `No such file or directory` or `required file not found` errors while trying to run the program.
One way to solve this, is to start a Alpine linux Docker container and execute the binary inside there.

Otherwise, one can also just reverse the flag printing function by hand, its nothing too complicated.

We'll make sure that this compatability issue doesn't happen again next year :)

If you have any more questions regarding this, make sure to join [our Discord](https://discord.gg/Vm7N64M7). Contacting via e-mail is also possible, however some of us typically respond faster via Discord.
