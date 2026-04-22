#!/usr/bin/env python3
import os
name = input("Input File Name: ")
filename_parts = name.split(".")

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
# deletes previous line if 'del' is entered,
    try:
        if len(input_parts) == 2 and input_parts[0] == "del":
            line_num = int(input_parts[1])
            lines.pop(line_num - 1)
            with open(path, "w", encoding="utf-8") as f:
                f.writelines(lines)
            print(f"Deleted Line {line_num}")
            continue
        if inp == "del":
            deleted_line = len(lines)
            lines.pop()
            with open(path, "w", encoding="utf-8") as f:
                f.writelines(lines)
            print(f"Deleted Line {deleted_line}")
            continue
    except IndexError:
        print("No more lines to delete!")
        continue

    with open(path, "a", encoding="utf-8") as f:
        f.write(inp + "\n")
