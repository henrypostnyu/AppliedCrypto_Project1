def decipher_with_key(ciphertext, key_map):
    # Replace each letter in ciphertext using key_map (a dictionary)
    return ''.join(key_map.get(char, char) for char in ciphertext)

# message to decrypt
ciphertext = "T NFOS FOZ SWPZ LOCGQA OZWAGQ RPJ ZPNA BCZ PQ DOG RA MTHA RA XTBAGZJ OG MTHA RA VAPZW"

# unused variable to track progress that has been made on the message
plaintext  = "I KNOW NOT WHAT COURSE OTHERS MAY TAKE BUT AS FOR ME GIVE ME LIBERTY OR GIVE ME DEATH"

key_map = {
    'A': 'E',
    'B': 'B',
    'C': 'U',
    'D': 'F',
    'F': 'N',
    'G': 'R',
    'H': 'V',
    'J': 'Y',
    'L': 'C',
    'M': 'G',
    'N': 'K',
    'O': 'O',
    'P': 'A',
    'Q': 'S',
    'R': 'M',
    'T': 'I',
    'S': 'W',
    'V': 'D',
    'W': 'H',
    'X': 'L',
    'Z': 'T',    
}

# Decipher using established key map
deciphered_text = decipher_with_key(ciphertext, key_map)
print("Deciphered Text:", deciphered_text)