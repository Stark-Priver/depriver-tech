---
title: "Inavyofanya kazi #06: how passwords are stored (hashing and salt)"
description: "Good systems never store your password. Why plain text is a disaster, how one-way hashing works, how login checks without knowing, what salt does, why slow hashes (bcrypt, Argon2) matter, and the two PHP functions you need."
date: 2027-02-23T19:00:00+03:00
status: live
tags: ["inavyofanya-kazi", "security", "backend", "kiswahili"]
carousel: how-passwords-are-stored
slides:
  - "Websites shouldn't know your password."
  - "Plain text is a disaster."
  - "Hashing: a one-way machine."
  - "How login checks without knowing."
  - "Add salt, so twins look different."
  - "Use a slow password hash."
  - "Two functions. That's it."
  - "How does your project store them?"
---

A good system doesn't know your password. It stores a scrambled fingerprint. *Hata wao hawajui.*

## Plain text is a disaster

If a database stores passwords as they are, one leak exposes every user, and they probably use the same password elsewhere. Red flag: if “forgot password” emails you your **old** password, the site stores it wrongly.

## Hashing: a one-way machine

A hash function turns `embe123` into something like `a8f3…91c`. The same input always gives the same output, a tiny change gives a completely different output, and you **can't** turn the output back. Like blending a mango: easy to make juice, impossible to rebuild the mango.

## How login checks

1. You type your password.
2. The server hashes it again, with the same settings.
3. It compares the result with the stored hash.
4. Match? You're in. No match? “Password si sahihi.”

The real password is never saved anywhere.

## Salt

Salt is random text added to each password before hashing, so two users with the same password get different hashes. It stops attackers using giant pre-computed tables of common passwords. Modern tools add salt for you.

## Slow is good

| Algorithm | For passwords? |
|---|---|
| bcrypt | Yes |
| Argon2 | Yes (modern choice) |
| scrypt | Yes |
| MD5 / SHA-1 | No, far too fast |
| SHA-256 alone | No, also too fast |

Slow for one login is fine. Slow for a billion guesses stops attackers.

## The code

```php
// register
$hash = password_hash($password, PASSWORD_DEFAULT);

// login
if (password_verify($password, $hash)) {
    echo "Karibu!";
}
```

Laravel's `Hash::make()` and Django's auth do this for you; in Python, use the `bcrypt` or `argon2` packages. Never write your own hashing.

**How does your project store passwords?** Check your FYP code today.
