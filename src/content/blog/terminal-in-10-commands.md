---
title: "The terminal in 10 commands (don't fear the black screen)"
description: "pwd, ls, cd, mkdir, touch, cp, mv, cat, grep and rm: the ten commands that make the terminal feel like home, plus shortcuts and a 10-minute practice challenge. Windows users: Git Bash or WSL."
date: 2027-01-02T19:00:00+03:00
status: live
tags: ["terminal", "linux", "skills", "kiswahili"]
carousel: terminal-in-10-commands
slides:
  - "The terminal in 10 commands."
  - "Every developer uses it daily."
  - "Where am I? pwd, ls, cd."
  - "Create, copy, move: mkdir, touch, cp, mv."
  - "Read, search, delete carefully: cat, grep, rm."
  - "Keys that save hours."
  - "The 10-minute challenge."
  - "Which command was new to you?"
---

Servers have no mouse. Git, npm, pip and Docker all start with a command. About ten commands are enough to feel at home. *Usiogope skrini nyeusi.* On Windows, use Git Bash or WSL: the commands are the same.

## Move around

| Command | Does |
|---|---|
| `pwd` | Show the folder you're in |
| `ls` | List what's in this folder |
| `cd folder` | Go into a folder (`cd ..` goes up) |

Press **Tab** to auto-complete names.

## Create, copy, move

| Command | Does |
|---|---|
| `mkdir images` | Make a folder |
| `touch index.html` | Make an empty file |
| `cp logo.png images/` | Copy (`cp -r` for folders) |
| `mv old.html new.html` | Move or rename |

There's no rename command: `mv old new` does it.

## Read, search, delete

| Command | Does |
|---|---|
| `cat notes.txt` | Print a file |
| `grep -r "TODO" .` | Search for text in files |
| `rm old.txt` | Delete a file, **forever** |

`rm` has no recycle bin. Never run `rm -rf` on something you didn't read.

## Keys that save hours

**Tab** auto-completes · **Up arrow** repeats previous commands · **Ctrl+C** stops what's running · **Ctrl+L** clears the screen · **Ctrl+R** searches your history · `command --help` explains any command.

## 10-minute challenge

1. `mkdir portfolio`, then `cd portfolio`
2. `touch index.html style.css`
3. Make an `images` folder and copy one photo into it
4. `mv style.css main.css`
5. `ls`, then `cd ..`

You just used seven of the ten.

**Which command was new to you?** Save this as your cheat sheet.
