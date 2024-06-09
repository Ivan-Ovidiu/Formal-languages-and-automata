# This is the main file that runs the emulator for the DFA.
from parser import load_file
from checker import validate_dfa
from emulator import emulator



dictionary = load_file("1_6_a.txt")
print(validate_dfa(dictionary, show_errors=1))
#print(dictionary)
emulator(dictionary)

