-- depriver.tech engagement database (Cloudflare D1). Visitors are stored only as salted hashes.

CREATE TABLE IF NOT EXISTS views (
  slug TEXT NOT NULL,
  visitor TEXT NOT NULL,
  day TEXT NOT NULL,
  PRIMARY KEY (slug, visitor, day)
);

CREATE TABLE IF NOT EXISTS likes (
  slug TEXT NOT NULL,
  visitor TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (slug, visitor)
);

-- status: published | pending (held for review) | hidden (removed by the owner)
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  slug TEXT NOT NULL,
  parent_id INTEGER,
  name TEXT NOT NULL,
  body TEXT NOT NULL,
  visitor TEXT NOT NULL,
  is_owner INTEGER NOT NULL DEFAULT 0,
  status TEXT NOT NULL DEFAULT 'published',
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  contact TEXT NOT NULL,
  body TEXT NOT NULL,
  visitor TEXT NOT NULL,
  is_read INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- simple per-visitor rate limits (comments, messages, AI questions)
CREATE TABLE IF NOT EXISTS hits (
  visitor TEXT NOT NULL,
  kind TEXT NOT NULL,
  bucket TEXT NOT NULL,
  n INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (visitor, kind, bucket)
);

CREATE INDEX IF NOT EXISTS views_slug ON views (slug);
CREATE INDEX IF NOT EXISTS likes_slug ON likes (slug);
CREATE INDEX IF NOT EXISTS comments_slug ON comments (slug, status);
