# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Obtain the names for the invites to add the email in a list
names = []

with open("./input/names/invited_names.txt") as file:
    for name in file:
        names.append(name.strip())
# print(names)

#  obtain the letter to read, edit and re-save in new location

with open("./input/letters/starting_letter.txt") as letter:
    lines = letter.readlines()

first_line = lines[0]
first_line_list = []
for name in names:
    x = first_line.replace("[name]", f"{name}")
    first_line_list.append(x.strip())

# print(first_line_list)
# append names and letter to new letter and save
index = 0
for name in names:
    name = open(f"./output/readytosend/{name}.txt", "w")
    name.writelines(first_line_list[index] + "\n")
    name.writelines(lines[1:])
    index += 1
