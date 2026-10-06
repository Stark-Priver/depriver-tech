---
title: "Programming exam? Don't memorise: how to study code for exams"
description: "How to prepare when the exam asks you to write and trace code on paper: why memorising fails, practising by hand, trace tables, past papers, study groups and what to do in the exam room."
date: 2026-11-17T19:00:00+03:00
status: live
tags: ["students", "exams", "study", "kiswahili"]
carousel: study-programming-for-exams
slides:
  - "Programming exam? Don't memorise."
  - "Memorising fails when the lecturer changes one detail."
  - "Practise the way you'll be tested: by hand, timed."
  - "Be the computer: trace code with a table."
  - "Past papers are gold."
  - "Teach it to a friend."
  - "In the exam room: five rules."
  - "Which exam is your hardest?"
---

Most programming exams ask you to **write and trace code on paper**. Memorised answers break the moment the question changes. *Usikariri, elewa.*

## Why memorising fails

You memorised “largest number in a list”. The exam asks for the smallest, or the second largest. Same idea, different code. Lecturers change one detail on purpose, and understanding survives that.

## Practise the way you'll be tested

- **Write code by hand**, on paper, with no autocomplete.
- **Time yourself.** A 10-mark question gets about 15 minutes.
- **Then type it and run it.** The computer marks your paper answer honestly.
- **Explain it out loud.** If you can't explain a line, you don't own it yet.

## Trace tables: be the computer

```python
total = 0
for i in range(1, 4):
    total = total + i
print(total)
```

| Step | i | total |
|---|---|---|
| Start | - | 0 |
| Loop 1 | 1 | 1 |
| Loop 2 | 2 | 3 |
| Loop 3 | 3 | 6 |

It prints **6**, because `range(1, 4)` stops before 4. Write every step; that's how you catch the tricky ones.

## Past papers are gold

1. Get three years of past papers from class reps, seniors or the library.
2. Solve one without notes, timed.
3. Mark it honestly: run your code and compare with seniors.
4. Two days later, redo only what you got wrong.

Topics repeat. After three papers you'll see what comes every year.

## Teach it to a friend

Study in a group of three or four. Each person teaches one topic (loops, arrays, functions, OOP) in 10 minutes. Swap and mark each other's past papers. Phones away for 50 minutes, then a break. If nobody can explain something, ask the lecturer this week, not on exam day.

## In the exam room

1. Read every question first, then start with the one you know best.
2. Plan before you write: three lines of steps in plain words.
3. Write clean, readable code with good names.
4. Stuck? Write the logic anyway. Steps and comments can still earn marks.
5. Check the edges: an empty list, zero, negative numbers.

And sleep. A rested brain debugs better than a tired one.

**Which exam is your hardest?** Comment the course code, and save this for revision week.
