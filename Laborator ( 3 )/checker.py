

def check(dictionary, show_errors=0):
    # Check if any section is empty
    for section_name in dictionary:
        if not dictionary[section_name]:
            if show_errors == 1:
                print(f"{section_name} section is empty")
            return 1

    # Check if states in Delta transitions are declared in States
    for transition in dictionary["Delta"]:
        if transition[0] not in dictionary["States"]:
            if show_errors == 1:
                print(f"State {transition[0]} not declared in section States")
            return 2
        if transition[2] not in dictionary["States"]:
            if show_errors == 1:
                print(f"State {transition[2]} not declared in section States")
            return 2

    # Check if symbols in Delta transitions are declared in Sigma
    for transition in dictionary["Delta"]:
        if transition[1] not in dictionary["Sigma"]:
            if show_errors == 1:
                print(f"Letter {transition[1]} not declared in section Sigma")
            return 2

    # Check if final states are declared in States
    for state in dictionary["Final States"]:
        if state not in dictionary["States"]:
            if show_errors == 1:
                print(f"Final state {state} not declared in section States")
            return 3

    # Check if there is exactly one starting state
    if len(dictionary["Starting State"]) != 1:
        if show_errors == 1:
            print("There are more than one starting states")
        return 3

    # Check if starting state is declared in States
    for state in dictionary["Starting State"]:
        if state not in dictionary["States"]:
            if show_errors == 1:
                print(f"State {state} not declared in section States")
            return 3

    return 0
