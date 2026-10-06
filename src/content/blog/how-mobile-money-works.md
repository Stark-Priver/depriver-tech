---
title: "Inavyofanya kazi #01: where your money goes when you send it"
description: "You send TZS 10,000 and seconds later it arrives. The five stops in between: your phone and PIN, the network, the checks, the ledger and the SMS, plus what money systems teach developers."
date: 2026-11-28T19:00:00+03:00
status: live
tags: ["inavyofanya-kazi", "fintech", "mobile-money", "kiswahili"]
carousel: how-mobile-money-works
slides:
  - "Where does your money go? Safari ya shilingi elfu kumi."
  - "Stop 1: you start the transfer."
  - "Stop 2: through the mobile network."
  - "Stop 3: checked in milliseconds."
  - "Stop 4: the money moves in a ledger."
  - "Stop 5: two SMS, one reference."
  - "What money systems teach developers."
  - "What should I explain next?"
---

You send TZS 10,000 to Juma. Seconds later he has it. Here's everything that happens in between, in five stops. This is **Inavyofanya kazi**, a series about how everyday tech works. *Safari ya shilingi elfu kumi.*

## Stop 1: you

You dial the USSD code or open the app, choose “send money”, enter Juma's number and the amount, then your **PIN**. Your PIN proves it's really you. Staff and agents will never ask for it. Your phone sends the request: from, to, amount, and the PIN check.

## Stop 2: the network

Your phone talks to the nearest tower, which sends the request through the operator's core network to the **mobile money platform**, the system that holds everyone's wallets. Because USSD works without internet, this reaches almost every phone.

## Stop 3: the checks

In milliseconds the platform checks: is the PIN correct? Is there enough balance for the amount plus the fee? Is it within the daily and per-transaction limits? Does it look like fraud? If any check fails, nothing moves and you get a failure SMS.

## Stop 4: the ledger

| Wallet | Before | After |
|---|---|---|
| You | 35,000 | 24,500 |
| Juma | 2,000 | 12,000 |
| Fee | | +500 |

*Example numbers only; fees vary by operator and amount.*

No cash travels. One database transaction subtracts from you and adds to Juma at the same moment. The real money behind e-money is kept in trust accounts at banks.

## Stop 5: the confirmation

Both of you get an SMS with the same **reference number**. Keep it: it's your proof if anything goes wrong. If you're on different networks, the operators record the transfer and settle with each other later.

## What developers can learn

- **All or nothing (atomic):** the debit and credit happen together, or neither happens.
- **Never twice (idempotent):** a repeated request must not send the money again.
- **Log everything:** every step has an ID you can trace.
- **Plan for failure:** timeouts, reversals and “pending” are normal states.

Database transactions are the place to start.

**What should I explain next?** Comment the tech you want explained.
