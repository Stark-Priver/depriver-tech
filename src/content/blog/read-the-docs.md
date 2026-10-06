---
title: "Read the docs: the skill that separates copiers from builders"
description: "Why documentation beats tutorials, the map every docs site shares (quickstart, guides, API reference, examples, changelog), how to read a function entry, matching versions, and a one-week docs-only challenge."
date: 2027-01-21T19:00:00+03:00
status: live
tags: ["skills", "learning", "students", "kiswahili"]
carousel: read-the-docs
slides:
  - "Read the docs."
  - "Tutorials age. Docs don't."
  - "Every docs site has the same map."
  - "Don't read it like a novel."
  - "How to read a function entry."
  - "Match the docs to your version."
  - "One week, docs only."
  - "Which docs do you read most?"
---

Tutorials teach you to copy. Docs teach you to build anything. *Soma maelekezo rasmi.*

## Why docs

They're written by the people who built the tool, updated with every version (a 2021 video may show code that no longer works), cheaper on your bundle than video, and reading them is a real job skill: at work, nobody makes a tutorial for your problem. Videos for your first steps, docs for everything after.

## The map

| Section | Use it to |
|---|---|
| Quickstart | Get it running in 10 minutes |
| Guides | Learn one topic step by step |
| API reference | Look up exact functions and options |
| Examples | Copy working code, then adapt |
| Changelog | See what changed between versions |

Always do the Quickstart first, even if it looks too easy.

## How to read

1. Know your question first: “How do I send a POST request with JSON?”
2. Use the search box (Ctrl+K or Ctrl+F).
3. Read the example first, then the explanation around it.
4. Run it yourself and change one thing.
5. Bookmark what you use often.

Seniors don't remember everything. They know where to look.

## Reading a function entry

```python
str.split(sep=None, maxsplit=-1)
# Returns a list of the words in the string, using sep as the separator.
"a,b,c".split(",")  # ["a", "b", "c"]
```

Look for the **name**, the **parameters** (`sep=None` means it's optional, with a default), what it **returns**, and the **example**.

## Match your version

Check your version (`python --version`, `php -v` or `package.json`), pick the same version in the docs, read the changelog when upgrading (look for “breaking changes” and “deprecated”), and if an old tutorial breaks, search the changelog for the function name. Half of “the tutorial doesn't work” is a version mismatch.

## The challenge

For one week, docs only: pick one tool (Laravel, React, Flask or Flutter), do its Quickstart with no YouTube, then build one tiny thing from the Guides. Post what you built and which page helped most.

**Which docs do you read most?** Comment your favourite docs site.
