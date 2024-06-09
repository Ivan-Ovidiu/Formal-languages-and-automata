def load_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line.strip() for line in lines if line.strip() and not line.startswith("#")]

    sections = {}
    current_section = None

    for line in filtered_lines:
        if line.endswith(":"):
            current_section = line[:-1]
            sections[current_section] = []
        elif current_section:
            if line == "End":
                current_section = None
            else:
                sections[current_section].append(line)

    delta_tuples = [tuple(transition.split(", ")) for transition in sections.get("Delta", [])]
    sections["Delta"] = tuple(delta_tuples)

    return sections



