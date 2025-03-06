from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import itertools
import time
import sys
import os

# if called from main directory
sys.path.append(os.path.abspath("./dist"))

from output import flag_ciphertext, ciphertext, plaintext, partial_key


# Function to split the key into k1 and k2, with the middle part disclosed
def split_key(k):
    k1 = k[:len(k) // 2]
    k2 = k[len(k) // 2:]
    return k1, k2

# Function to perform double AES decryption with two different keys
def aes_256_decrypt(ciphertext, key):
    k1, k2 = split_key(key)

    # AES decryption with k2
    cipher2 = AES.new(k2, AES.MODE_ECB)
    intermediate_ciphertext = unpad(cipher2.decrypt(ciphertext), AES.block_size)

    # AES decryption with k1
    cipher1 = AES.new(k1, AES.MODE_ECB)
    plaintext = unpad(cipher1.decrypt(intermediate_ciphertext), AES.block_size)

    return plaintext


# Function to encrypt with the first key half (k1)
def aes_encrypt_with_partial_key(plaintext, key):
    k1, k2 = split_key(key)
    cipher = AES.new(k1, AES.MODE_ECB)
    return cipher.encrypt(pad(plaintext, AES.block_size))

# Function to decrypt with the second key half (k2)
def aes_decrypt_with_partial_key(ciphertext, key):
    k1, k2 = split_key(key)
    cipher = AES.new(k2, AES.MODE_ECB)
    decrypted  = cipher.decrypt(ciphertext)
    try:
        return unpad(decrypted, AES.block_size)
    except ValueError:
        # Return the raw decrypted message if unpad fails
        return decrypted

def aes_decrypt_with_padding(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)


# Meet-in-the-middle attack implementation
def mitm_attack(partial_key, plaintext, ciphertext):
    middle_key = partial_key[3:-3]  # The known middle part of the key
    possible_first_3 = itertools.product(range(256), repeat=3)  # All possible first 3 bytes
    possible_last_3 = itertools.product(range(256), repeat=3)   # All possible last 3 bytes

    start = time.time()
    # Dictionary to store all encryptions from the first half
    encryptions = {}

    print("generate the list for key 1 !")
    # Encrypt with all possible first 3-byte values of k1
    for first_3 in possible_first_3:
        

        k1 = bytes(first_3) + middle_key + b'\x00\x00\x00'
        encrypted = aes_encrypt_with_partial_key(plaintext, k1)

        encryptions[encrypted] = k1
 


    print("check key 2 !")
    # Decrypt with all possible last 3-byte values of k2 and compare
    for last_3 in possible_last_3:
        k2 = b'\x00\x00\x00' + middle_key + bytes(last_3)
        decrypted = aes_decrypt_with_partial_key(ciphertext, k2)

        # If there's a match, we have found the correct key
        if decrypted in encryptions:
            print("found")
            correct_k1 = encryptions[decrypted]
            correct_k2 = k2
        
            print("correct_k2 : ", correct_k2)
            print("correct_k1 : ", correct_k1)


            end = time.time()
            print("time of simple search", end - start)
            return correct_k1, correct_k2
    
    

    return None  # No match found





# Run the MITM attack
found_k1, found_k2 = mitm_attack(partial_key, plaintext, ciphertext)

first_16_from_k1 = found_k1[:16]
# Take the last 16 bytes from found_k2
last_16_from_k2 = found_k2[16:]
# Combine the two parts
combined_key = first_16_from_k1 + last_16_from_k2
print("Combined Key:", combined_key)



decrypted_plaintext = aes_256_decrypt(flag_ciphertext, combined_key)
print("Decrypted Plaintext:", decrypted_plaintext.decode())

# simple method takes  140s bzw. 219s

