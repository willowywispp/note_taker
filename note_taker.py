#!/usr/bin/env python3
import os
name = input("Input File Name: ")
filename_parts = name.split(".")

# if no file type is input, assumes .txt
if len(filename_parts) == 1:
    path = f"/home/willow/work/note_taker/notes/{name}.txt"
else:
    path = f"/home/willow/work/note_taker/notes/{name}"

def delete_line(lines, index=None):
    try:
        if index is None:
            lines.pop()
        else:
            lines.pop(index - 1)
    except IndexError:
        pass
    return lines

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
# deletes previous line if 'del' is entered,
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


    with open(path, "a", encoding="utf-8") as f:
        f.write(inp + "\n")
