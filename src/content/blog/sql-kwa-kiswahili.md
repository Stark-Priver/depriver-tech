---
title: "SQL kwa Kiswahili: talk to a database"
description: "SQL explained in plain Kiswahili with one simple table: SELECT (nipe), WHERE (pale ambapo), ORDER BY and LIMIT (panga, chukua), GROUP BY (kwa kila) and JOIN (unganisha)."
date: 2027-03-09T19:00:00+03:00
status: live
tags: ["sql", "databases", "kiswahili", "students"]
carousel: sql-kwa-kiswahili
slides:
  - "SQL kwa Kiswahili. Ongea na database."
  - "A table is like a daftari."
  - "SELECT: nipe…"
  - "WHERE: pale ambapo…"
  - "ORDER BY: panga kwa…"
  - "GROUP BY: kwa kila…"
  - "JOIN: unganisha majedwali."
  - "Write a query in the comments."
---

SQL reads almost like a sentence. Say it in Kiswahili first, then write it. *Ongea na database.*

## The table

**wanafunzi** (students):

| id | jina | mkoa | alama |
|---|---|---|---|
| 1 | Asha | Mbeya | 78 |
| 2 | Juma | Dodoma | 64 |
| 3 | Neema | Mbeya | 91 |
| 4 | Baraka | Arusha | 55 |

A **table** (jedwali) is like a daftari, a **row** (mstari) is one student, and a **column** (safu) is one detail, like `mkoa`.

## SELECT: “nipe…”

*“Nipe jina na alama kutoka wanafunzi.”*

```sql
SELECT jina, alama
FROM wanafunzi;
```

`SELECT *` means “nipe kila kitu”; use it only while exploring.

## WHERE: “pale ambapo…”

*“Nipe wanafunzi pale ambapo mkoa ni Mbeya.”*

```sql
SELECT jina, alama FROM wanafunzi
WHERE mkoa = 'Mbeya';
```

Result: Asha (78), Neema (91). Text goes in single quotes; numbers don't.

## ORDER BY and LIMIT: “panga, chukua”

*“Nipe watatu bora, panga kwa alama kushuka.”*

```sql
SELECT jina, alama FROM wanafunzi
ORDER BY alama DESC
LIMIT 3;
```

`DESC` = kushuka (biggest first), `ASC` = kupanda.

## GROUP BY: “kwa kila…”

*“Hesabu wanafunzi kwa kila mkoa.”*

```sql
SELECT mkoa, COUNT(*) AS idadi
FROM wanafunzi
GROUP BY mkoa;
```

Mbeya 2, Dodoma 1, Arusha 1. `SUM`, `AVG` and `MAX` work the same way: sales per day is `GROUP BY tarehe`.

## JOIN: “unganisha majedwali”

*“Nipe jina na ada iliyolipwa, ukiunganisha na jedwali la ada.”*

```sql
SELECT w.jina, a.kiasi
FROM wanafunzi w
JOIN ada a ON a.mwanafunzi_id = w.id;
```

Tables share an id, and JOIN matches the rows where the ids are equal.

**Your turn:** write a query for *wanafunzi wenye alama zaidi ya 70* in the comments.
