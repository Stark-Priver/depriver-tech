---
title: "Code ya Wiki #01: Kwa nini wastani si sahihi? (Python)"
description: "Spot the bug: Find the average mark of the class. It runs, but it's wrong. The bug, the fix and the lesson: Lists start at index 0. Loop over the items, not the numbers."
date: 2026-11-21T19:00:00+03:00
status: live
tags: ["code-ya-wiki", "debugging", "python", "kiswahili"]
carousel: code-ya-wiki-01
slides:
  - "Code ya Wiki #01: kosa liko wapi? Kwa nini wastani si sahihi?"
  - "It runs, but it's wrong. Expected 70.0, got 43.33...."
  - "Found it: line 4."
  - "The fix."
  - "Never get caught again."
  - "Did you find it before slide 3?"
---

**Code ya Wiki** is a weekly “spot the bug”. Try it before you read the answer. *Kosa liko wapi?*

**Goal:** find the average mark of the class.

```python
marks = [80, 60, 70]

total = 0
for i in range(1, len(marks)):
    total = total + marks[i]

average = total / len(marks)
print(average)
```

| Expected | Got |
|---|---|
| `70.0` | `43.33...` |

**Hint:** Count how many marks the loop actually adds. Is the first student included?

## The bug

range(1, len(marks)) starts at index 1, so marks[0] (the 80) is never added. Python lists start counting at 0.

## The fix

```python
marks = [80, 60, 70]

total = 0
for mark in marks:
    total = total + mark

average = total / len(marks)
print(average)
```

## The lesson

**Lists start at index 0. Loop over the items, not the numbers.**

- **Loop over items directly.** for mark in marks: no index, no off-by-one.
- **Use built-ins.** sum(marks) / len(marks) does it in one line.
- **Test with tiny data.** Three numbers you can add in your head.

*Hesabu kuanzia sifuri.* Did you find it before the answer? Comment “nimepata” or “nimekwama”, and send me a bug for the next Code ya Wiki.
