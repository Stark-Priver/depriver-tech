---
title: "Jenga kwa Tanzania #03: build apps that work on a TZS 150,000 phone"
description: "Your app works on your phone. Does it work on your customer's entry-level Android? Keep apps small, fix images, design for weak signal, respect data and storage, and test on a real cheap phone."
date: 2026-12-17T19:00:00+03:00
status: live
tags: ["jenga-kwa-tanzania", "mobile", "performance", "kiswahili"]
carousel: build-for-cheap-phones
slides:
  - "Works on your phone. Does it work on hers?"
  - "Your users are not on flagships."
  - "Small apps get installed."
  - "Images are the biggest leak."
  - "Design for weak signal."
  - "Respect their MBs."
  - "Borrow a cheap phone and test."
  - "Which app is too heavy on your phone?"
---

Your app flies on your phone. On your customer's entry-level Android it shows “Inapakia…” forever. *Jenga kwa simu za watu halisi.*

## The reality

Many users have entry-level phones with little RAM and older Android versions, storage that's always full of photos and WhatsApp media, expensive data, and networks that drop on the road and upcountry. Design for the phone your customer has, not the one you have.

## Keep it small

- **Fewer libraries.** Every package adds weight.
- **Android App Bundles**, so the Play Store sends each phone only what it needs.
- **On the web, less JavaScript.** Ship plain HTML first.
- **Check the size every release** and notice when it grows.

Ask: “Would I download this on a full phone with 300 MB of data?”

## Fix the images

A photo straight from the camera can be many times heavier than it needs to be. Serve the size you display, use WebP (or AVIF), compress, and lazy-load images below the screen. Fixing images alone often makes a site several times lighter.

## Design for weak signal

Test with throttling (Chrome DevTools “Slow 3G”, or the Android emulator's network settings), show something fast (skeleton screens, cached content), retry instead of crashing (“Hakuna mtandao. Jaribu tena.”), and keep API responses small and paginated. Users blame your app, not the network.

## Respect data and storage

Cache what doesn't change, let users choose quality (“download on Wi-Fi only”), clean up temp files, and work offline where you can.

## Test on a real cheap phone

| Check | Pass if |
|---|---|
| App size | Small enough to keep |
| First screen | Shows in a few seconds |
| Slow 3G | Still usable, no crash |
| No network | Clear message, data kept |
| Low storage | Installs and runs |
| Old Android | Works, nothing cut off |

Even easier: ask a relative to use your app while you watch quietly.

**Which app is too heavy on your phone?** Comment it, no shame.
