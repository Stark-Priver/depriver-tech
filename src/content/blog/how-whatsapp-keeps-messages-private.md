---
title: "Inavyofanya kazi #04: can WhatsApp read your chats? End-to-end encryption explained"
description: "How end-to-end encryption keeps WhatsApp messages private, public and private keys as padlocks, what encryption can't protect (backups, metadata, an unlocked phone), five settings to turn on, and lessons for developers."
date: 2027-01-14T19:00:00+03:00
status: live
tags: ["inavyofanya-kazi", "security", "privacy", "kiswahili"]
carousel: how-whatsapp-keeps-messages-private
slides:
  - "Can WhatsApp read your chats?"
  - "Locked on your phone, opened only on theirs."
  - "Open padlocks and secret keys."
  - "Your message's trip."
  - "What encryption can't protect."
  - "Five settings to turn on today."
  - "What builders should learn."
  - "Did you turn on two-step?"
---

Short answer: no, not the message contents. Long answer: end-to-end encryption, and the things it doesn't protect. *Siri kati yako na yeye.*

## End-to-end encryption

End-to-end encryption (E2E) means the message is scrambled on your phone and unscrambled only on the receiver's phone. The server in the middle only ever sees scrambled text.

## Padlocks and keys

- **Public key:** like an open padlock. Juma's phone gives copies to anyone who wants to message him.
- **Private key:** the only key that opens those padlocks. It's created on Juma's phone and never leaves it.

You lock the message with Juma's padlock; only his phone can open it. This is public-key cryptography, and WhatsApp uses the Signal protocol.

## The trip

You type and send → it's locked on your phone → the server stores and delivers the locked box → Juma's phone opens it → two blue ticks. Group chats, voice notes and calls are protected the same way.

## What it can't protect

- **An unlocked phone.** Anyone holding it can read everything.
- **Screenshots and forwards.** Once shared, it's out.
- **Unencrypted backups.** Backups are only E2E if you turn that on.
- **Metadata.** Who you talk to and when can still be seen by the service.
- **Scams.** Encryption can't stop you sending money to a fake “boss”.

## Five settings for today

1. **Two-step verification:** Settings > Account. A PIN stops number hijacks.
2. **End-to-end encrypted backup:** Settings > Chats > Chat backup.
3. **A screen lock** on your phone.
4. **Check linked devices** and remove any you don't recognise.
5. **Never share the 6-digit code.**

## For developers

Use HTTPS everywhere, never invent your own cryptography (use proven libraries like libsodium), hash passwords instead of storing them, and keep secrets on the server, never inside the app.

**Did you turn on two-step?** Comment “nimewasha”, then send this to the family group.
