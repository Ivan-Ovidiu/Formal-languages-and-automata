def validate_dfa(data, show_errors=0):
    # Verify if any section is empty
    for section in data:
        if not data[section]:
            if show_errors:
                print(f"{section} section is empty")
            return 1

    # Validate the 'Delta' section
    for delta in data["Delta"]:
        if delta[0] not in data["States"] or delta[2] not in data["States"]:
            if show_errors:
                print(
                    f"State {delta[0] if delta[0] not in data['States'] else delta[2]} not declared in section States")
            return 2
        if delta[1] not in data["Sigma"]:
            if show_errors:
                print(f"Letter {delta[1]} not declared in section Sigma")
            return 2

    # Check if 'Final States' are in 'States' section
    for final_state in data["Final States"]:
        if final_state not in data["States"]:
            if show_errors:
                print(f"State {final_state} not declared in section States")
            return 3

    # Ensure there is exactly one starting state
    if len(data["Starting State"]) != 1:
        if show_errors:
            print("There are multiple starting states")
        return 3

    # Confirm the starting state is in 'States' section
    if data["Starting State"][0] not in data["States"]:
        if show_errors:
            print(f"State {data['Starting State'][0]} not declared in section States")
        return 3

    return 0
