---
title: "Jenga kwa Tanzania #02: accept mobile money payments in your app"
description: "How “Lipa kwa simu” works inside an app: direct operator APIs vs aggregators, the payment flow from button to callback, the rules that keep money safe, sandbox testing and going live."
date: 2026-12-01T19:00:00+03:00
status: live
tags: ["jenga-kwa-tanzania", "payments", "fintech", "backend", "kiswahili"]
carousel: mobile-money-in-your-app
slides:
  - "“Lipa kwa simu” inside your app."
  - "Direct or through an aggregator."
  - "From “Lipa” to “Paid”: the flow."
  - "Trust the callback, not the button."
  - "Rules that keep money safe."
  - "Test every outcome in the sandbox."
  - "Live keys need a business."
  - "What app would you add payments to?"
---

Almost every Tanzanian business app needs mobile money. Here's how the flow works and the rules that keep money safe. *Malipo ndani ya mfumo wako.*

## Two roads

- **Direct:** integrate one operator's API (for example an operator's open API portal). One network per integration, more control.
- **Aggregator:** one API for many networks, cards and banks (for example Selcom, AzamPay or ClickPesa). The fastest way to start.

Start with one aggregator sandbox and learn the flow once. Always check the provider's current docs.

## The flow

1. The customer taps **Lipa** and enters their phone number.
2. Your server calls the provider with the amount, phone number and your order ID.
3. The customer's phone shows a **PIN prompt** (a USSD push).
4. The customer enters their PIN and the money moves on the provider's side.
5. The provider calls your **callback** URL with success or failure and a reference.
6. You mark the order paid and show the receipt.

Payment finishes on the provider's side. Your app waits for the callback.

## The callback

```python
@app.post("/payments/callback")
def callback():
    data = verify(request)  # signature
    order = find(data["order_id"])
    if order.paid:
        return ok()  # already done
    if data["status"] == "SUCCESS":
        order.mark_paid(data["ref"])
    return ok()
```

Field names differ per provider. The important line is `verify`: anyone can send a fake “SUCCESS”.

## Golden rules

- **Never trust the frontend.** Only the provider's confirmation counts.
- **Verify callbacks:** check the signature, or query the provider for the status.
- **Handle it once (idempotent):** callbacks can arrive twice. Don't deliver twice.
- **Save every reference:** order ID, provider reference, time and amount.
- **Pending is normal.** Show “inasubiri”, then update.

## Test every outcome

| Test case | Expected |
|---|---|
| PIN correct | Order paid, receipt |
| Wrong PIN / cancel | Order stays unpaid |
| No response (timeout) | Shows pending, retries |
| Callback sent twice | Delivered once |
| Not enough balance | Clear failure message |

A working sandbox demo is a strong project to show employers.

## Going live

Live keys usually need a registered business with KYC documents, an agreement and per-transaction fees (ask for current rates), a security review (HTTPS, secret keys only on the server) and a support plan for “nimelipa” calls. Freelancers: use the client's business account, never collect money in your own.

**What app would you add payments to?** Comment your idea.
