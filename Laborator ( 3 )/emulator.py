def nfa_emulator(nfa_dict):
    input_string = input("Enter the string to check: ")
    states = nfa_dict["States"]
    starting_state = nfa_dict["Starting State"][0]
    final_states = set(nfa_dict["Final States"])
    sigma = nfa_dict["Sigma"]
    delta = nfa_dict["Delta"]

    def get_next_states(current_states, input_symbol):
        next_states = set()
        for state in current_states:
            for transition in delta:
                if transition[0] == state and transition[1] == input_symbol:
                    next_states.add(transition[2])
        return next_states

    current_states = {starting_state}
    for symbol in input_string:
        if symbol not in sigma:
            return False
        current_states = get_next_states(current_states, symbol)

    return any(state in final_states for state in current_states)