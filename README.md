# note_taker

A simple terminal-based note taking CLI. Opens or creates a text file, then lets you append, edit, and delete lines in a live-updating terminal view.

## Usage

```
python note_taker.py
```

## Setup

On first run, you'll be prompted to enter a directory to store your notes. This path is saved to `config.txt` in the script's directory and reused on every subsequent run. To change it, just delete `config.txt` and restart the script.

Both `~` and relative paths like `./notes` are supported.

## Commands

| Command | Description |
|---|---|
| *(any text)* | Appends a new line to the file |
| `del` | Deletes the last line |
| `del <n>` | Deletes line number `n` |
| `edit <n> <text>` | Replaces line `n` with `text` |
| `q` | Exits the program |

## License

GPL-3.0
