def load_file(file_name):
    text_clean = []
    with open(file_name, 'r') as text:
        for line in text:
            if line.strip():
                if line[0] != "#":
                    text_clean.append(line.strip())

    content = {}
    in_section = 0
    for cuvant in text_clean:
        if cuvant[len(cuvant)-1] == ":":
            in_section = 1
            section_name = cuvant[:len(cuvant)-1]
            content[section_name] = []
            continue

        if in_section == 1:
            if cuvant == "End":
               in_section=0
            else:
                content[section_name].append(cuvant)
    temp=[]
    for transition in content["Rules"]:
        temporar = transition.split(" -> ")
        temporar[1] = tuple(temporar[1].split(" "))
        temp.append(tuple(temporar))
    content["Rules"] = tuple(temp)
    return(content)


