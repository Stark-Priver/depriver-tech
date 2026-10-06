---
title: "Code ya Wiki #04: Kwa nini kila mtu anakaribishwa? (Python)"
description: "Spot the bug: Welcome only Asha and Juma to the admin page. It runs, but it's wrong. The bug, the fix and the lesson: Each side of “or” is its own test. Compare both, or use “in”."
date: 2027-02-13T19:00:00+03:00
status: live
tags: ["code-ya-wiki", "debugging", "python", "kiswahili"]
carousel: code-ya-wiki-04
slides:
  - "Code ya Wiki #04: kosa liko wapi? Kwa nini kila mtu anakaribishwa?"
  - "It runs, but it's wrong. Expected Huna ruhusa. (for Neema), got Karibu admin!."
  - "Found it: line 3."
  - "The fix."
  - "Never get caught again."
  - "Did you find it before slide 3?"
---

**Code ya Wiki** is a weekly “spot the bug”. Try it before you read the answer. *Kosa liko wapi?*

**Goal:** welcome only Asha and Juma to the admin page.

```python
name = input("Jina lako: ")

if name == "Asha" or "Juma":
    print("Karibu admin!")
else:
    print("Huna ruhusa.")
```

| Expected | Got |
|---|---|
| `Huna ruhusa. (for Neema)` | `Karibu admin!` |

**Hint:** Read the if line the way Python reads it. What is “Juma” on its own?

## The bug

Python reads it as (name == "Asha") or ("Juma"). A non-empty string is always true, so everyone gets in.

## The fix

```python
name = input("Jina lako: ")

if name in ("Asha", "Juma"):
    print("Karibu admin!")
else:
    print("Huna ruhusa.")
```

## The lesson

**Each side of “or” is its own test. Compare both, or use “in”.**

- **Write full comparisons.** name == "Asha" or name == "Juma"
- **Or use in.** name in ("Asha", "Juma") is cleaner.
- **Test the “no” case too.** Always try a name that should be refused.

*Jaribu jibu la hapana pia.* Did you find it before the answer? Comment “nimepata” or “nimekwama”, and send me a bug for the next Code ya Wiki.
