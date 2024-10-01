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

    #Run through all combinations of initial settings

    #numerical representations (A=0,etc) for initial position for rL (i), rM (j), RR (k)
    i = 0 
    j = 0 
    k = 0
    
    while k < 26: #while third rotor hasnt exhausted all positions
        #convert the numbers to a list and store as a string
        #mod 26 to avoid resetting values to zero each rotor cycles through its initital position
        initial_settings = str(int_list_to_string([i%26,j%26,k%26]))

        #pass the string into the run enigma with the message
        result = run_enigma(initial_settings,m)
        
        if(result == m2): #Check the result against the known value
            found = True
            break #if a match is found stop looking

        i += 1 #otherwise keep incrementing until we try all 3 letter combinations
        if(i > 0 and i % 26 == 0):
            j += 1 
        if(j > 0 and j % 26 == 0):
            j = 0
            k += 1

    #output
    if(found):
        print("************************INITIAL SETTINGS FOUND after ",i," cycles:  ",initial_settings)
    else:
        print("All initial settings searched")


    


