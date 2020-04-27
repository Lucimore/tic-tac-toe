text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
user_input = int(input())
new_list = []
for n in text:
    for inner_list_el in n:
        if len(inner_list_el) <= user_input:
            new_list.append(inner_list_el)
print(new_list)
