# Cracking Affine Cipher
# c = Ap + b mod 26

#letter 'T' is encrypted to 'H' and 'O' to 'E'.

import typing
from typing import List

ciphertext = 'QJKESREOGHGXXREOXEO'
plaintext = 'CRYPTOISFUN'

#letter 'T' is encrypted to 'H' and 'O' to 'E'.

# Function to compute modular inverse of a mod m using the extended Euclidean algorithm
def modular_inverse(a: int, m: int) -> int:
    # Using pow(a, -1, m) to compute the modular inverse
    # pow(a, -1, m) computes the modular inverse of a under modulo m
    return pow(a, -1, m)


# Encrypt one character by converting to its corresponding number and applying the Affine Cipher formula
def encrypt_one_integer(plaintext: int) -> int:
    return ((5 * plaintext) + 9) % 26

# Decrypt one character by applying the inverse Affine Cipher formula
def decrypt_one_integer(ciphertext: int) -> int:
    # Modular inverse of 5 mod 26 is 21
    a_inverse = modular_inverse(5, 26)
    return (a_inverse * (ciphertext - 9)) % 26


# Convert string to list of integers (A=0, B=1, ..., Z=25)
def string_to_int_list(string: str) -> List[int]:
    # Initialize an empty list to store the integers
    ints = []

    # Iterate over each character in the string
    for char in string:
        # Convert each character to its corresponding integer (A=0, ..., Z=25)
        int_value = ord(char) - ord('A')
        ints.append(int_value)

    return ints

# Convert list of integers to string (0=A, 1=B, ..., 25=Z)
def int_list_to_string(ints: List[int]) -> str:
    # Convert each integer back to its corresponding character
    char_list = [chr(i + ord('A')) for i in ints]

    # Join the list of characters into a single string
    return ''.join(char_list)

# Ensure string contains only uppercase ASCII characters
def filter_uppercase_ascii(s: str) -> str:
    # Filter out any non-uppercase ASCII characters
    uppercase_chars = [char for char in s if char.isupper()]

    # Join the list of uppercase characters into a single string
    return ''.join(uppercase_chars)


# Encrypt the entire plaintext using the Affine Cipher formula
def encrypt_string(plaintext: str) -> str:

    # make sure it's in uppercase
    plaintext = plaintext.upper()

    # make sure only uppercase ASCII characters are in the string
    plaintext = filter_uppercase_ascii(plaintext)

    plaintext_int_list = string_to_int_list(plaintext)  # Convert string to list of integers
    encrypted_integers = [encrypt_one_integer(n) for n in plaintext_int_list]  # Encrypt each integer
    return int_list_to_string(encrypted_integers)  # Convert back to letters

# Decrypt the entire ciphertext using the Affine Cipher formula
def decrypt_string(ciphertext: str) -> str:
    # Convert the ciphertext string to a list of integers
    encrypted_ints = string_to_int_list(ciphertext)
    decrypted_ints = [decrypt_one_integer(c) for c in encrypted_ints]  # Decrypt each integer
    return int_list_to_string(decrypted_ints)  # Convert back to letters

def solve_encryption():
    knownletters = {
        "T":"H",
        "O":"E"}
    
    knownlettersValue = {} 
    knownlettersValue.update("A","B")
    
    
    print(knownletters)
    #knownPs = string_to_int_list([knownletters.keys])
    #print(knownPs) 
    # c = (Ap + b) mod 26
    # 4 =(A*14 + b) mod 26


if __name__ == '__main__':

    #solve_encryption()
    print(modular_inverse(11,26))
    # print plaintext
    #print("plaintext:            "+plaintext)


    # Test our plaintext
    encrypted_text = encrypt_string(plaintext)
    #print(f"ciphertext:           {encrypted_text}")

    # Decrypt the ciphertext
    decrypted_text = decrypt_string(encrypted_text)
    #print(f"Decrypted ciphertext: {decrypted_text}")