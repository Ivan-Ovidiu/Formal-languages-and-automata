import emulator
import checker
import parser

dictionary = parser.load_file("1_7_b.txt")
print(checker.check(dictionary, show_errors=1))
print(dictionary)
print(emulator.nfa_emulator(dictionary))
