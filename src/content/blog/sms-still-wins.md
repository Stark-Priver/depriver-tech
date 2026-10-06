---
title: "Jenga kwa Tanzania #05: SMS still wins (and how to send it from your app)"
description: "SMS reaches every phone with no data or app. What people build with it, how an SMS gateway works, sending one SMS in a few lines of code, sender IDs, consent and length rules, and two-way SMS."
date: 2027-01-19T19:00:00+03:00
status: live
tags: ["jenga-kwa-tanzania", "sms", "backend", "kiswahili"]
carousel: sms-still-wins
slides:
  - "SMS still wins."
  - "Reaches people apps can't."
  - "What people build with SMS."
  - "From your code to their phone."
  - "Send one SMS in a few lines."
  - "Send SMS responsibly."
  - "Let people reply."
  - "What SMS service would you build?"
---

Every phone gets SMS: no data, no app, no smartphone needed. That's why clinics, schools and banks still use it. *Ujumbe mfupi, kazi kubwa.*

## Why SMS

It works on every phone, arrives even when the bundle is finished, people open messages from known senders quickly, and a registered sender name builds trust. Use your app for rich features and SMS for the messages people must see.

## What people build

Reminders (clinic visits, loan dates) · fee and bill balances · login and payment codes (OTP) · order updates (“mzigo wako umefika”) · alerts (prices, weather, outbreaks) · surveys (“reply 1, 2 or 3”). An SMS reminder system is a simple, useful final year project.

## How it works

Your app decides to send → calls an **SMS gateway API** (for example Africa's Talking, Beem or NextSMS) → the gateway passes it to the networks → the phone receives it from your sender name → a delivery report comes back.

## The code

```python
import requests

def send_sms(phone, text):
    return requests.post(GATEWAY_URL,
        headers={"apiKey": API_KEY},
        data={"to": phone,
              "message": text,
              "from": "KLINIKI"})
```

A generic example: each gateway has its own URL, field names and SDK, so copy them from its docs. Keep `API_KEY` in an environment variable, never in GitHub.

## Send responsibly

- **Register your sender name.** Sender IDs need approval and it takes time, so start early.
- **Only message people who agreed**, with an easy way to stop.
- **Mind the length:** 160 characters per part; emojis and some symbols cut it to 70.
- **Right time of day:** no marketing SMS at 11 p.m.

You pay per SMS part, so short messages save money.

## Two-way SMS

> KLINIKI: Kumbusho: miadi yako ni kesho saa 3. Jibu 1 kuthibitisha, 2 kubadilisha.

The reply reaches your server through the gateway, like a webhook. Fewer missed appointments is something a clinic will pay for.

**What SMS service would you build?** Comment your idea.
