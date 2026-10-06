---
title: "Git in 7 commands: never lose your code again"
description: "Git explained for students in seven commands: init, status, add, commit, log, push and pull, with good commit messages and a daily routine."
date: 2027-02-16T19:00:00+03:00
status: live
tags: ["git", "skills", "students", "kiswahili"]
carousel: git-in-7-commands
slides:
  - "Git in 7 commands."
  - "Save points for your code."
  - "Start tracking a project: git init, git status."
  - "Save a checkpoint: git add, git commit."
  - "See your history: git log."
  - "Send it to GitHub: git push, git pull."
  - "The daily routine."
  - "What's your worst “lost code” story?"
---

Git gives your code save points, like a game. Break something? Go back to the last save. *Hifadhi kila hatua.*

## Why Git

Go back in time, no more `final_FINAL2.zip`, work in a team, and your GitHub becomes your CV.

## The seven commands

| # | Command | Does |
|---|---|---|
| 1 | `git init` | Start Git in this folder |
| 2 | `git status` | What changed? (Safe to run anytime) |
| 3 | `git add .` | Choose what to save |
| 4 | `git commit -m "..."` | Save it with a message |
| 5 | `git log --oneline` | Every save, newest first |
| 6 | `git push` | Upload your commits to GitHub |
| 7 | `git pull` | Download your team's commits |

## Good commit messages

Bad: `update`, `stuff`. Good: `Add login form validation`, `Fix total when cart is empty`. Say what the commit **does**, in a few words. In group projects, the log shows who did what.

## First push

```
git remote add origin <your repo URL>
git push -u origin main
```

## The daily routine

`git pull` → write code → `git status` → `git add` + `git commit` → `git push`. Commit small and often.

**What's your worst “lost code” story?** Share it, and send this to your group project team.
