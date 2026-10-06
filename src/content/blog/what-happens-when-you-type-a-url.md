---
title: "Inavyofanya kazi #02: what happens when you type a URL and press Enter"
description: "In under a second your browser finds a server, makes a secure connection, asks for the page and draws it. DNS, HTTPS, HTTP requests, status codes and rendering, explained simply, plus how to watch it in DevTools."
date: 2026-12-15T19:00:00+03:00
status: live
tags: ["inavyofanya-kazi", "web", "networking", "kiswahili"]
carousel: what-happens-when-you-type-a-url
slides:
  - "You press Enter. Sekunde moja, safari ndefu."
  - "Stop 1: DNS finds the address."
  - "Stop 2: shake hands and lock the line."
  - "Stop 3: ask for the page."
  - "Stop 4: the server answers."
  - "Stop 5: the browser draws it."
  - "See it yourself in DevTools."
  - "Which stop surprised you?"
---

You type `depriver.tech` and press Enter. In under a second, five things happen. It's also a classic interview question. *Sekunde moja, safari ndefu.*

## 1. DNS: find the address

Computers use numbers (IP addresses), not names. DNS is the internet's phonebook. Your browser first checks its own memory, then asks a DNS resolver (usually from your network provider), which answers with the server's IP address. Like tapping “Juma” and your phone dialling his number.

## 2. Connect: shake hands, lock the line

Your device and the server open a connection (TCP), then secure it with **HTTPS** (TLS): they agree on secret keys so nobody in between can read the traffic, and the server shows a certificate proving it really is depriver.tech. The padlock icon means this worked.

## 3. Request: ask for the page

```
GET /blog HTTP/1.1
Host: depriver.tech
Accept: text/html
```

`GET` means “give me”. Forms use `POST`: “here's data”. Every page, image and button press is a request like this.

## 4. Response: the server answers

| Code | Means |
|---|---|
| 200 OK | Here's the page |
| 301 | It moved, go here instead |
| 404 | Not found |
| 500 | The server crashed |

Then it sends the HTML. Status codes tell you whose problem it is: yours or the server's.

## 5. Render: the browser draws it

It reads the HTML, fetches the CSS, JavaScript and images (often dozens more requests), applies the CSS and runs the JavaScript. Slow sites are usually slow because of huge images and too much JavaScript.

## See it yourself

Open DevTools (F12 or Ctrl+Shift+I), go to the **Network** tab and reload. Every row is one request with its status, size and time. Sort by size to find what to fix first, and try “Slow 3G” to feel what users on bad networks feel.

**Which stop surprised you?** Comment 1 to 5.
