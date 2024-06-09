import emulator
import parser

dictionary = parser.load_file("2_6_c.txt")
print(dictionary)
print(emulator.generate_random(dictionary, dictionary['Starting Symbol'][0]))