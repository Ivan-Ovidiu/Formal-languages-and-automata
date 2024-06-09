# This is the main file that runs the emulator for the DFA.
from c_parser import load_file
from dfa_checker import validate_dfa
from emulator import emulator



dictionary = load_file("1_6_a.txt")
print(validate_dfa(dictionary, show_errors=1))
#print(dictionary)
emulator(dictionary)

