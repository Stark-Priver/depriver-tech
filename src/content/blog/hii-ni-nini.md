---
title: "Hii ni nini? Guess the file from what's inside"
description: "A light holiday quiz: five files every developer meets (package.json, .gitignore, .env, Dockerfile, README.md). See what's inside, guess the name, then learn what each one does."
date: 2026-12-24T19:00:00+03:00
status: live
tags: ["quiz", "students", "developer-tools", "kiswahili"]
carousel: hii-ni-nini
slides:
  - "Hii ni nini? Guess the file."
  - "File 1: name, version, scripts, dependencies."
  - "File 2: node_modules, .env, *.log."
  - "File 3: DB_PASSWORD and API keys."
  - "File 4: FROM, WORKDIR, COPY, RUN, CMD."
  - "File 5: # Duka App and how to run it."
  - "The answers."
  - "What did you score?"
---

A light quiz for the holidays. Five files every developer meets. Guess each name from its contents, then check your score. *Taja jina la faili.*

## The answers

1. **package.json** lists a JavaScript project's name, scripts and the packages it needs. `npm install` reads it.
2. **.gitignore** tells Git which files never to commit: secrets, build output, `node_modules`, logs and junk.
3. **.env** holds secret settings and keys (database passwords, API keys). Never commit it and never share it. Commit a `.env.example` with fake values instead.
4. **Dockerfile** has the instructions to build a container, so the same app runs the same way everywhere.
5. **README.md** is the front page of your project: what it is and how to run it. Recruiters read it first.

**Score:** 5/5 senior · 3/5 getting there · 1/5 just starting (that's fine).

**What did you score?** Comment it, challenge a classmate, and suggest a file for the next quiz.
