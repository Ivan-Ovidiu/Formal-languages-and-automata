def emulator(dfa):
    user_input = input("Input the string: ").split()
    state = dfa["Starting State"][0]

    for char in user_input:
        for rule in dfa["Delta"]:
            if rule[0] == state and rule[1] == char:
                state = rule[2]
                break

    if state in dfa["Final States"]:
        print("The string is correct")
    else:
        print("The string is not correct")
