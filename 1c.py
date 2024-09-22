# Cracking Affine Cipher
# c = Ap + b mod 26,  solution: A = 11, B = 6

#letter 'T' is encrypted to 'H' and 'O' to 'E'.
#Plaintext: IFYOUBOWATALLBOWLOW
#Key: GRCNYJUFQBMXITEPALWHSDOZKV
#ciphertext = 'QJKESREOGHGXXREOXEO'

import typing
from typing import List

ciphertext = 'QJKESREOGHGXXREOXEO'

ciphertext_from_plaintext = { "T":"H", "O":"E"}
plainInt_from_plaintext = {}
cipherInt_from_plaintext = {}

# Function to compute modular inverse of a mod m using the extended Euclidean algorithm
def modular_inverse(a: int, m: int) -> int:
    # Using pow(a, -1, m) to compute the modular inverse
    # pow(a, -1, m) computes the modular inverse of a under modulo m
    return pow(a, -1, m)


# Encrypt one character by converting to its corresponding number and applying the Affine Cipher formula
def encrypt_one_integer(affine_a,affine_b,plaintext: int) -> int:
    return ((affine_a * plaintext) + affine_b) % 26

# Decrypt one character by applying the inverse Affine Cipher formula
def decrypt_one_integer(affine_a,affine_b,ciphertext: int) -> int:
    # Modular inverse of 5 mod 26 is 21
    a_inverse = modular_inverse(affine_a, 26)
    return (a_inverse * (ciphertext - affine_b)) % 26


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

# Decrypt the entire ciphertext using the Affine Cipher formula
def decrypt_string(affine_a, affine_b,ciphertext: str) -> str:
    # Convert the ciphertext string to a list of integers
    encrypted_ints = string_to_int_list(ciphertext)
    decrypted_ints = [decrypt_one_integer(affine_a,affine_b,c) for c in encrypted_ints]  # Decrypt each integer
    return int_list_to_string(decrypted_ints)  # Convert back to letters


def solve_encryption():   
    
    #Map the known information to integer value / set up all the dictionaries
    affine_A = 0 
    affine_b = 0 
    for keys in ciphertext_from_plaintext:
        p = keys
        pInt = string_to_int_list(p)[0]

        c = ciphertext_from_plaintext[p]
        cInt = string_to_int_list(c)[0]

        plainInt_from_plaintext[p]=pInt
        cipherInt_from_plaintext[p]=cInt

    '''
    the conguence class of a mod 26 is well defined under multiplication and division
    [a] mod 26 + [b] mod 26 = [a+b] mod 26 
    and 
     [a] mod 26 * [b] mod 26 = [ab] mod 26 

     we can we can rearrange  C = (Ap + b) mod 26 
    C = A mod 26 * p mod 26 + b mod 26
    yielding

    A mod 26 * p1 mod 26 + b mod 26 - (A mod 26 * p2 mod 26 + b mod 26) = C2 - C1, allowing us to solve for the value of Ax and then try
    possible valyes of A.  

    A mod 26 * (p1 - p2) = c1 - c2 
    

    '''
    p1minusp2 = (plainInt_from_plaintext["T"] - plainInt_from_plaintext["O"]) 
    c1minusc2 = cipherInt_from_plaintext["T"] - cipherInt_from_plaintext["O"]

    #Now we know that A * factor modulu 26 is equivalent to c1minusc2 e.g. we can try values
    #for A 5A mod 26 = 3 and we can try values for A. 
    i = 0
    r = 0
    while r != c1minusc2:      
       r = (p1minusp2 * i) % 26
       affine_A = i
       i += 1

    #Now that we have A we can solve for b:
    i = 0
    r = 0
    x = (affine_A * plainInt_from_plaintext["T"]) % 26
    while True:
        r = x + (i % 26)
        if(r % 26 == cipherInt_from_plaintext["T"]):
            affine_b = i
            break
        i += 1

    return [affine_A,affine_b]

affine_Ab_values = solve_encryption()

decrypted_text = decrypt_string(affine_Ab_values[0], affine_Ab_values[1],ciphertext)
print(f"Decrypted ciphertext: {decrypted_text}")