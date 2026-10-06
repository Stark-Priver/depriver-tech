---
title: "Code ya Wiki #03: Kwa nini wote wamelipa? (SQL)"
description: "Spot the bug: Mark that student 1042 has paid school fees. It runs, but it's wrong. The bug, the fix and the lesson: UPDATE and DELETE without WHERE touch every row."
date: 2027-01-09T19:00:00+03:00
status: live
tags: ["code-ya-wiki", "debugging", "sql", "kiswahili"]
carousel: code-ya-wiki-03
slides:
  - "Code ya Wiki #03: kosa liko wapi? Kwa nini wote wamelipa?"
  - "It runs, but it's wrong. Expected 1 row updated, got 2,318 rows updated."
  - "Found it: line 2, 3."
  - "The fix."
  - "Never get caught again."
  - "Did you find it before slide 3?"
---

**Code ya Wiki** is a weekly “spot the bug”. Try it before you read the answer. *Kosa liko wapi?*

**Goal:** mark that student 1042 has paid school fees.

```sql
-- Asha (id 1042) has paid her fees
UPDATE students
SET fee_paid = 1;
```

| Expected | Got |
|---|---|
| `1 row updated` | `2,318 rows updated` |

**Hint:** The query says what to change. Does it say which student?

## The bug

There's no WHERE. Without it, UPDATE changes every row in the table: the whole school is now marked as paid.

## The fix

```sql
-- Asha (id 1042) has paid her fees
UPDATE students
SET fee_paid = 1
WHERE id = 1042;
```

## The lesson

**UPDATE and DELETE without WHERE touch every row.**

- **SELECT first.** Run SELECT * FROM students WHERE id = 1042 and check the result.
- **Use a transaction.** BEGIN, run it, check, then COMMIT or ROLLBACK.
- **Back up before big changes.** And never practise on the live database.

*Chagua kwanza, badilisha baadaye.* Did you find it before the answer? Comment “nimepata” or “nimekwama”, and send me a bug for the next Code ya Wiki.
