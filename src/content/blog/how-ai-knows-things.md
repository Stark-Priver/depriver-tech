---
title: "Inavyofanya kazi #05: how does AI “know” things?"
description: "AI models predict the next word from patterns learned on huge amounts of text. Tokens, why AI is weaker in Kiswahili, why it makes things up, training cutoffs, and five rules to use it well."
date: 2027-01-28T19:00:00+03:00
status: live
tags: ["inavyofanya-kazi", "ai", "students", "kiswahili"]
carousel: how-ai-knows-things
slides:
  - "How does AI “know” things? It predicts the next word."
  - "It read a huge amount of text."
  - "One word at a time."
  - "It reads in pieces (tokens)."
  - "Why it sometimes makes things up."
  - "What it knows, and when."
  - "Use it like a smart assistant."
  - "Has AI ever lied to you?"
---

“Mji mkuu wa Tanzania ni ___”. An AI model doesn't look the answer up. It predicts the most likely next word. *Inabashiri neno linalofuata.*

## Training

Models are trained on huge amounts of text (books, websites, code, conversations). They learn **patterns**: which words tend to follow which, in what situations. Then people rate answers so the model learns to follow instructions helpfully. It doesn't keep a table of facts; it predicts.

## One word at a time

For “Habari za ___” it might rank *asubuhi*, *leo*, *jioni*, *kazi*… then pick one, add it, and predict the next word again, hundreds of times, very fast. (The numbers on the slides are an illustration; real models choose from tens of thousands of options.)

## Tokens

Models read text in pieces called tokens. Many models split Swahili into more pieces than English, because they saw less Swahili text in training. That's one reason AI is often weaker in Kiswahili, and why more good Swahili data matters.

## Why it makes things up

Ask for “three history books about Tanzania with their authors” and it may invent a convincing title and author. It writes what a real answer would **look** like. If it doesn't know, it can still sound confident. Confident is not the same as correct.

## What it knows, and when

It has a **training cutoff** and may not know recent news, prices or versions. Some tools can search the web, but can still misread pages. It only sees what you give it (paste your code or document), and it doesn't remember you unless the app has a memory feature. For anything recent, check the official source.

## Use it well

1. **Give context:** who you are, what you're building, what you tried.
2. **Ask it to explain.** Understanding beats copying, especially for exams.
3. **Check facts and code.** Run it, and verify names, dates and sources.
4. **Ask for sources, then open them.** A link you didn't click proves nothing.
5. **Keep private data out:** no passwords, IDs or client secrets.

You are responsible for what you submit, not the AI.

**Has AI ever lied to you?** Comment the funniest wrong answer.
