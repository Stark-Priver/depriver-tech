---
title: "Code ya Wiki #05: Kwa nini hii ni hatari? (PHP)"
description: "Spot the bug: Find a user by the phone number typed in the login form. It runs, but it's wrong. The bug, the fix and the lesson: Never paste user input into SQL. Use prepared statements."
date: 2027-03-06T19:00:00+03:00
status: live
tags: ["code-ya-wiki", "debugging", "php", "kiswahili"]
carousel: code-ya-wiki-05
slides:
  - "Code ya Wiki #05: kosa liko wapi? Kwa nini hii ni hatari?"
  - "It runs, but it's wrong. Expected Only that user's row, got Every user's row."
  - "Found it: line 3, 4."
  - "The fix."
  - "Never get caught again."
  - "Did you find it before slide 3?"
---

**Code ya Wiki** is a weekly “spot the bug”. Try it before you read the answer. *Kosa liko wapi?*

**Goal:** find a user by the phone number typed in the login form.

```php
$phone = $_POST["phone"];

$sql = "SELECT * FROM users
        WHERE phone = '$phone'";
$user = $db->query($sql);
```

| Expected | Got |
|---|---|
| `Only that user's row` | `Every user's row` |

**Hint:** Imagine someone types a quote mark and a bit of SQL into the phone box instead of a number.

## The bug

The input is pasted straight into the SQL. Typing ' OR '1'='1 changes the query itself. This is SQL injection, a top cause of data leaks.

## The fix

```php
$phone = $_POST["phone"];

$stmt = $db->prepare(
    "SELECT * FROM users WHERE phone = ?");
$stmt->execute([$phone]);
```

## The lesson

**Never paste user input into SQL. Use prepared statements.**

- **Prepared statements, always.** PDO prepare() + execute() in PHP, the same idea in every language.
- **Validate input.** A phone number should only contain digits.
- **Use the framework's tools.** Laravel's Eloquent and query builder do this for you.

*Usimwamini mtumiaji.* Did you find it before the answer? Comment “nimepata” or “nimekwama”, and send me a bug for the next Code ya Wiki.
