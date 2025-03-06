import random
import sys
import time


def multi_mod_encrypt(mods, length):
    ct = ""
    for x in range(length):  
        result = x
        for m in mods:
            result = result % m
        ct += str(result)
    return ct


def multi_mod_decrypt(ct):
    found_mods = []

    for i in range(1, len(ct)//2, 1):
        if(ct[0:i] == ct[i:2*i] ):
            print("found new mod = ", i)
            found_mods.append(i)
    return found_mods

# m0, m1,... are odd (except the last one) and mi is not a multiple of m(i-1).
# The flag is  SSH{mod_numbers_are_m0+m1+m2+m3} ONLY THE FIRST 4
# for example if "m0=501, m1=101, m2=31, m3=13, m4=5, m5=2 =-> SSH{mod_numbers_are_501+101+31+13}"
length = 100000
...
mods = [35183, 16579, 5103, 1989, 649, 165, 63, 31, 13, 5, 2]

# Good property: Make sure that mi > 2*m(i+1)
has_property = True 
for i in range(len(mods)-1):
    if (mods[i] // mods [i+1]) < 2:
        has_property = False
if(length // mods[i-1]) < 2:
    has_property = False     
        

if has_property:
    print("has property")
    ct = multi_mod_encrypt(mods, length)
    print(ct)


with open("./../dist/L2_ct.txt", "r") as file:
    binary_string = file.read().strip()

found = multi_mod_decrypt(binary_string)

print(list(reversed(found)))
print(mods)

if set(mods) == set(found):
    print("The lists are equal.")
else:
    print("The lists are not equal.")