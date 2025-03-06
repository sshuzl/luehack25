# Writeup - number_guesser1

## Idea

With each guess you make, you can discover on bit of the number we search. As the number is 2048-bit we need 2048 guesses to reveal the number.

## Implementation

The input is checked in binary form and only checks for the bit-length of the smaller number. The bits are check starting from the LSB. Therefore, you can reconstruct the number bit by bit by always setting the next MSB to one, and only revert it to 0 if the compare returns false.