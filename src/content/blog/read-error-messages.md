---
title: "Read the error message. It's telling you what's wrong"
description: "Stop panicking at red text. The three parts of every error, reading from the bottom up, six errors to learn by heart, searching like a developer, isolating the bug and asking for help well."
date: 2026-12-03T19:00:00+03:00
status: live
tags: ["debugging", "skills", "students", "kiswahili"]
carousel: read-error-messages
slides:
  - "Read the error. It's telling you."
  - "Three parts, every time: where, what, why."
  - "Start from the last line."
  - "Learn these six errors by heart."
  - "Google like a developer."
  - "Still stuck? Shrink the problem."
  - "Ask for help the right way."
  - "What error haunts you the most?"
---

Beginners see red text and panic. Seniors read it. *Kosa linakuambia kitu.*

## Three parts, every time

```
Traceback (most recent call last):
  File "sales.py", line 12, in <module>
    total = total + sale["amount"]
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

1. **Where:** `sales.py`, line 12.
2. **What:** `TypeError`, a wrong type.
3. **Why:** adding a number and text.

The fix: `sale["amount"]` is text, so use `int(sale["amount"])`.

## Read from the bottom up

- The **last line** is the real message. Read it slowly, word by word.
- Then find **your** file in the trace and skip lines from libraries.
- Go to that exact line and check the values with `print()` or the debugger.
- The bug may be one line earlier: a missing bracket often shows up on the next line.

## Six errors to know by heart

| Error | Usually means |
|---|---|
| SyntaxError | A typo: bracket, colon, quote |
| NameError | A name misspelt or not defined |
| TypeError | Wrong type: text vs number |
| IndexError | That list position doesn't exist |
| KeyError | That dictionary key doesn't exist |
| 404 / 500 | Page missing / server crashed |

JavaScript, PHP and Java have the same ideas with different names.

## Search like a developer

- Weak: `my code is not working python help`
- Strong: `python TypeError unsupported operand int and str`

Copy the exact error type and message, remove your own names and paths, and add the language or framework. Using AI? Paste the error and ask it to **explain**, then fix it yourself.

## Still stuck? Shrink the problem

1. Print the values: what is `sale` really? `print(type(sale))`.
2. Comment out half the code. Still broken? The bug is in the other half.
3. Make the smallest example (five lines) that shows the same error.
4. Explain it out loud to a rubber duck.

## Ask for help the right way

Write: your **goal**, what you **expected**, what you **got** (the full error), what you **tried**, and the **smallest code** that shows it. Never send “guys code yangu haifanyi kazi” with a blurry photo of your screen. Half of all bugs are found while writing the question.

**What error haunts you the most?** Comment it and I'll explain it.
