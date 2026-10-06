---
title: "Jenga kwa Tanzania #04: offline-first apps that keep working without network"
description: "Save locally, sync later. Why offline-first matters for shops, field agents and upcountry users, how a sync queue works, handling conflicts, tools for web, Android and Flutter, and good offline UX."
date: 2027-01-07T19:00:00+03:00
status: live
tags: ["jenga-kwa-tanzania", "mobile", "architecture", "kiswahili"]
carousel: offline-first-apps
slides:
  - "No network? Keep working."
  - "The network will drop."
  - "Save locally. Sync later."
  - "Every change waits in a queue."
  - "Two phones edit the same thing?"
  - "Tools that do the heavy lifting."
  - "Tell the user what's happening."
  - "Which app should work offline?"
---

Offline-first apps save work on the phone and sync when the network comes back. Perfect for shops, pharmacies, field agents and upcountry users. *Mtandao ukikata, kazi iendelee.*

## Why

Field agents collect data in villages and on roads, a shop can't wait for 4G to sell, bundles run out, and power and network cuts are normal days, not accidents. Treat “no network” as a normal state, not an error.

## The idea

1. The user saves an order; it's written to the phone's own database first.
2. It shows as **“Inasubiri”** and the user keeps working.
3. When the network comes back, the app notices automatically.
4. The queue is sent to the server, oldest first.
5. Each item is marked **“Imetumwa”** when the server confirms it.

The phone is the first home of the data; the server is the second.

## The sync queue

Every change waits in a queue with an ID created on the phone (a UUID), so nothing clashes when items reach the server. The server must accept the same item twice without duplicating it, because retries happen.

## Conflicts

Two phones edit the same thing? Choose a rule per type of data: **last write wins** (fine for notes and settings), **merge** (stock: add both sales, don't overwrite the count), **ask the user** when it really matters, or **record events, not totals** (“sold 2” merges more easily than “stock = 18”).

## Tools

| Platform | Local storage + sync |
|---|---|
| Web (PWA) | Service Worker + IndexedDB |
| Android | Room + WorkManager |
| Flutter | Drift, sqflite or Hive |
| Any app | Firestore offline persistence |

Make one screen work offline first, then grow.

## Good offline UX

A clear offline banner (“Offline · 3 zinasubiri”), never lose data, sync on its own with no “upload” button to forget, and show a green “Imetumwa” when it's done. Users trust apps that never lose their work.

**Which app should work offline?** Comment one that fails you.
