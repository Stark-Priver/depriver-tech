---
title: "Code ya Wiki #02: Kwa nini jumla ni kubwa hivi? (JavaScript)"
description: "Spot the bug: Add the delivery fee (TZS 2,000) to the price typed in a form. It runs, but it's wrong. The bug, the fix and the lesson: Form values are strings. Convert them before you do maths."
date: 2026-12-19T19:00:00+03:00
status: live
tags: ["code-ya-wiki", "debugging", "javascript", "kiswahili"]
carousel: code-ya-wiki-02
slides:
  - "Code ya Wiki #02: kosa liko wapi? Kwa nini jumla ni kubwa hivi?"
  - "It runs, but it's wrong. Expected Jumla: 7000, got Jumla: 50002000."
  - "Found it: line 2."
  - "The fix."
  - "Never get caught again."
  - "Did you find it before slide 3?"
---

**Code ya Wiki** is a weekly “spot the bug”. Try it before you read the answer. *Kosa liko wapi?*

**Goal:** add the delivery fee (TZS 2,000) to the price typed in a form.

```js
const input = document.querySelector("#price");
const price = input.value;
const delivery = 2000;

const total = price + delivery;
console.log("Jumla:", total);
```

| Expected | Got |
|---|---|
| `Jumla: 7000` | `Jumla: 50002000` |

**Hint:** The user typed 5000. What type of value does a form input give you?

## The bug

Form inputs always give text (a string). "5000" + 2000 joins the text instead of adding: "50002000".

## The fix

```js
const input = document.querySelector("#price");
const price = Number(input.value);
const delivery = 2000;

const total = price + delivery;
console.log("Jumla:", total);
```

## The lesson

**Form values are strings. Convert them before you do maths.**

- **Convert input to numbers.** Number(value) or parseInt(value, 10).
- **Check for NaN.** If the user types letters, show an error.
- **Log the type.** console.log(typeof price) shows "string" right away.

*Maandishi si namba.* Did you find it before the answer? Comment “nimepata” or “nimekwama”, and send me a bug for the next Code ya Wiki.
