def load_file(file_name):
    text_clean = []
    with open(file_name, 'r') as file:
        text_clean = [line.strip() for line in file if line.strip() and line[0] != "#"]

    content = {}
    section = None

    for line in text_clean:
        if line.endswith(":"):
            section = line[:-1]
            content[section] = []
        elif line == "End":
            section = None
        elif section:
            content[section].append(line)

    if "Delta" in content:
        content["Delta"] = tuple(tuple(item.split(", ")) for item in content["Delta"])

    return content