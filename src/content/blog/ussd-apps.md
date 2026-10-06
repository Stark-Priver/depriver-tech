---
title: "Jenga kwa Tanzania #01: build a USSD app (*150*00# is an app too)"
description: "USSD works on every phone in Tanzania, without internet. How a USSD session reaches your server, the CON/END pattern in 10 lines of code, design rules, testing for free and what going live takes."
date: 2026-11-19T19:00:00+03:00
status: live
tags: ["jenga-kwa-tanzania", "ussd", "backend", "kiswahili"]
carousel: ussd-apps
slides:
  - "*150*00# is an app too."
  - "Works on every phone in Tanzania."
  - "From *123# to your server."
  - "CON continues, END finishes: the code."
  - "Short menus win: design rules."
  - "Test it today, for free."
  - "Going live is a business step."
  - "USSD apps worth building."
  - "What would you build with USSD?"
---

Millions of Tanzanians use USSD every day: mobile money, bundles, banking. It works on any phone, with no internet and nothing to install. Most students never learn to build it. *Programu bila internet.* This is the first post in **Jenga kwa Tanzania**, a series about building tech for how Tanzania really lives.

## Why USSD

- **No internet, no smartphone needed.** A TZS 25,000 kitochi works perfectly.
- **Nothing to install.** Dial a code and the menu appears.
- **People already trust it**, because mobile money and banks use it.
- **Fast and cheap for the user.**

Your users may not have data. They almost always have airtime.

## How it works

1. The user dials a code, e.g. `*123*45#`.
2. The mobile network receives it.
3. A USSD gateway (aggregator) turns it into a web request.
4. **Your server** reads the choice and builds the next menu.
5. The text goes back to the phone.

For you, a USSD app is just a web endpoint that returns text.

## The code

```python
@app.post("/ussd")
def ussd():
    text = request.form["text"]
    if text == "":
        return "CON Karibu\n1. Bei\n2. Oda"
    if text == "1":
        return "END Sukari: TZS 3,000"
    return "END Asante!"
```

This is the Africa's Talking style: `CON` keeps the session open, `END` closes it, and `text` holds the user's choices so far (like `1*2`). Other gateways work similarly; check their docs.

## Design rules

- **Keep each screen short.** USSD screens hold about 182 characters.
- **Numbered choices, five or six at most.** Add 0 for back and 00 for the main menu.
- **Kiswahili first.** “Salio”, not “Account balance”.
- **Sessions time out fast.** Few steps, and never ask people to type long text.
- **Always confirm before money moves:** “Lipa TZS 3,000? 1. Ndiyo 2. Hapana”.

## Test it today, for free

1. Write the endpoint in Flask, Express or Laravel.
2. Expose it: deploy free, or use a tunnel like ngrok while testing.
3. Open a gateway sandbox. Africa's Talking, for example, has a free USSD simulator.
4. Click through every path, including mistakes.
5. Record a demo video for your portfolio.

## Going live

Going live is a business step: you need a USSD code (shared or dedicated) through an aggregator and the networks, live codes usually go to registered organisations, there are monthly costs, and telecom and data protection rules apply. Ask providers for current requirements and prices before you promise a client anything. As a student, build the demo now and sell it to a client who already has a code.

## Ideas worth building

School fees balance for parents · clinic appointments with SMS reminders · crop prices for farmers · SACCO and VICOBA balances · shop orders from a wholesaler · water bill checks. Any of these is a strong, very Tanzanian final year project.

**What would you build with USSD?** Comment your idea.
