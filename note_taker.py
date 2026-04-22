#!/usr/bin/env python3
from os import system
name = input("Input File Name: ")
parts = name.split(".")

# if no file type is input, assumes .txt
if len(parts) == 1:
    path = f"/home/willow/work/note_taker/notes/{name}.txt"
else:
    path = f"/home/willow/work/note_taker/notes/{name}"

open(path, "a", encoding="utf-8").close()
while True:

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

# clears the terminal and writes existing numbered lines
    system("clear")
    for i, line in enumerate(lines, start=1):
        print(f"Line {i}: {line.strip()}")

    inp = input(f"\nLine {len(lines) + 1}: ")

    if inp == "q":
        print("Exiting...")
        exit()
# deletes previous line if 'del' is entered,
    try:
        if inp == "del":
            lines.pop()
            with open(path, "w", encoding="utf-8") as f:
                f.writelines(lines)
            print(f"Deleted Line {len(lines) + 1}")
            continue
    except IndexError:
        print("No more lines to delete!")
        continue

    with open(path, "a", encoding="utf-8") as f:
        f.write(inp + "\n")
