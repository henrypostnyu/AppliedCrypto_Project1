#!pip install py-enigma
from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine
from typing import List


def run_enigma(initial_display,message):
    #stepping is the notch
    rL = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q') 
    rM = Rotor('my rotor2', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=5, stepping='V')
    rR = Rotor('my rotor3', 'ESOVPZJAYQUIRHXLNFTGKDCMWB', ring_setting=10, stepping='J')

    reflector = Rotor('my reflector', 'YRUHQSLDPXNGOKMIEBFZCWVJAT')
    pb = Plugboard.from_key_sheet('AK BZ CG DL FU HJ MX NR OY PW')

    machine = EnigmaMachine([rL, rM, rR], reflector, pb) # Params = rotors, reflector, plugboard
    machine.set_display(initial_display) # set rotor positions or use its default
    position = machine.get_display() # read rotor position

    c = machine.process_text(message)
    return c

def int_list_to_string(ints: List[int]) -> str:
    # Convert each integer back to its corresponding character
    char_list = [chr(i + ord('A')) for i in ints]
    # Join the list of characters into a single string
    return ''.join(char_list)

if __name__ == '__main__':
    #m = 'Enigma machine is powerful for Q'
    m = 'WVUVJCSQBFLEJGFNIZNIGYGOCWSUVNCIIIA'
    m2 = 'ATTACKXATXXXXXXATXATLANTICXZXISLAND'
    print('\nm = ',m)
    found = False

    i = 0
    j = 0
    k = 0

    while k < 26:
        initial_settings = str(int_list_to_string([i%26,j%26,k%26]))
        result = run_enigma(initial_settings,m)
        
        if(result == m2):
            found = True
            break

        i += 1
        if(i > 0 and i % 26 == 0):
            j += 1
        if(j > 0 and j % 26 == 0):
            j = 0
            k += 1

    if(found):
        print("************************INITIAL SETTINGS FOUND after ",i," cycles:  ",initial_settings)
    else:
        print("All initial settings searched")


    


