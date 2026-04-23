#!/usr/bin/env python3
import os
name = input("Input File Name: ")
filename_parts = name.split(".")

def delete_line(lines, index=None):
    try:
        if index is None:
            lines.pop()
        else:
            lines.pop(index - 1)
    except IndexError:
        pass
    return lines

def edit_line(lines, index, message):
    lines.pop(index - 1)
    lines.insert(index - 1, message)
    return lines

# if no file type is input, assumes .txt
if len(filename_parts) == 1:
    path = f"/home/willow/work/note_taker/notes/{name}.txt"
else:
    path = f"/home/willow/work/note_taker/notes/{name}"

open(path, "a", encoding="utf-8").close()
while True:

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

# clears the terminal and writes existing numbered lines
    os.system("clear")
    for i, line in enumerate(lines, start=1):
        print(f"Line {i}: {line.strip()}")

    inp = input(f"\nLine {len(lines) + 1}: ")
    input_parts = inp.split(" ")

    if inp == "q":
        print("Exiting...")
        exit()
# deletes previous line is del is entered without line number using delete_line() function
# deletes line n del n using delete_line() function
    if len(input_parts) == 2 and input_parts[0] == "del":
        lines = delete_line(lines, int(input_parts[1]))
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        continue
    if inp == "del":
        lines = delete_line(lines)
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        continue

# replaces line n with whatever is written in the terminal using edit_line() function
    if len(input_parts) > 2 and input_parts[0] == "edit":
        try:
            edit_index = int(input_parts[1])
            message = " ".join(input_parts[2:]) + "\n"
            lines = edit_line(lines, edit_index, message)
            with open(path, "w", encoding="utf-8") as f:
                f.writelines(lines)
            continue
        except ValueError:
            pass


# writes the input and a newline to the file (keep at bottom)
    with open(path, "a", encoding="utf-8") as f:
        f.write(inp + "\n")
