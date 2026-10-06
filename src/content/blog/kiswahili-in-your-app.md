---
title: "Jenga kwa Tanzania #06: your app should speak Kiswahili"
description: "Localising apps for Tanzanian users: why language builds trust, natural Kiswahili vs literal translation, translation files (i18n), what breaks (length, money, dates, plurals), testing with real users and the tools for each stack."
date: 2027-02-18T19:00:00+03:00
status: live
tags: ["jenga-kwa-tanzania", "localisation", "ux", "kiswahili"]
carousel: kiswahili-in-your-app
slides:
  - "Your app should speak Kiswahili."
  - "Language is trust."
  - "Translate meaning, not words."
  - "Never hard-code your text."
  - "What breaks when you translate."
  - "Ask real users, not Google."
  - "Built-in tools for every stack."
  - "Which app needs Kiswahili most?"
---

“Make payment” or “Lipa”? For most of your users, the second one is instant. *Ongea lugha ya mtumiaji.*

## Why

People understand faster (no guessing what “Proceed” means), make fewer mistakes with money, call support less, and you reach parents, traders and farmers, not only graduates. The best apps offer both languages and remember the user's choice.

## Translate meaning, not words

| English | Natural Kiswahili |
|---|---|
| Log in | Ingia |
| Balance | Salio |
| Make payment | Lipa |
| Settings | Mipangilio |
| An error occurred | Kuna tatizo. Jaribu tena. |
| Are you sure? | Una uhakika? |

Use the words people already see in mobile money menus.

## Never hard-code text

```json
// en.json                       // sw.json
{ "pay": "Make payment" }       { "pay": "Lipa" }
```

```js
button.text = t("pay")
```

The code asks for a key; the language file gives the words. This is internationalisation (i18n). Even English-only apps should use keys from day one.

## What breaks

- **Longer text:** Kiswahili phrases are often longer, so buttons must stretch.
- **Money format:** TZS 15,000, not $15.00.
- **Dates and days:** Jumatatu, 12 Januari 2027; use the locale.
- **Plurals:** “1 oda”, “oda 3”; plan for both forms.

## Test with people

Test with people from different regions, stay formal but friendly in money and health apps, keep a glossary so the same thing has the same word everywhere, and read it out loud. Machine translation is fine for a first draft; a person must check it.

## Tools

Android: `res/values-sw/strings.xml` · Flutter: `intl` and `.arb` files · React/web: i18next · Laravel: `lang/sw/*.php` · locale code `sw` or `sw-TZ`.

**Which app needs Kiswahili most?** Comment the app and one word it gets wrong.
