-- Views and likes for depriver.tech. Visitors are stored only as salted hashes.
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
CREATE INDEX IF NOT EXISTS views_slug ON views (slug);
CREATE INDEX IF NOT EXISTS likes_slug ON likes (slug);
