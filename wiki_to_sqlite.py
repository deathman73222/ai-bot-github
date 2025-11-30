#!/usr/bin/env python3
"""Convert per-article .txt files produced by wiki_dumps.py into a sqlite database.

This script reads <outdir>/<lang>/articles/*.txt and writes a sqlite DB at
<outdir>/<lang>/wikipedia.db with tables `articles` and `search_index` compatible
with `ai_bot/modules/wikipedia_offline.py`.
"""
from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path
import os
import re
import json
from typing import Optional


def create_db(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY,
            title TEXT UNIQUE NOT NULL,
            content TEXT NOT NULL,
            summary TEXT,
            last_updated TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS search_index (
            id INTEGER PRIMARY KEY,
            article_id INTEGER NOT NULL,
            keyword TEXT NOT NULL,
            FOREIGN KEY (article_id) REFERENCES articles(id)
        )
    ''')
    conn.commit()
    return conn


def insert_article(conn: sqlite3.Connection, title: str, content: str) -> None:
    cursor = conn.cursor()
    summary = content[:500]
    cursor.execute('''
        INSERT OR REPLACE INTO articles (title, content, summary, last_updated)
        VALUES (?, ?, ?, datetime('now'))
    ''', (title, content, summary))
    conn.commit()
    # get last id
    cursor.execute('SELECT id FROM articles WHERE title = ?', (title,))
    row = cursor.fetchone()
    if not row:
        return
    aid = row[0]
    # index keywords from title
    for kw in re.findall(r"\w+", title.lower()):
        cursor.execute(
            'INSERT INTO search_index (article_id, keyword) VALUES (?, ?)', (aid, kw))
    conn.commit()


def build_from_articles(articles_dir: Path, db_path: Path, max_articles: Optional[int] = None) -> int:
    conn = create_db(db_path)
    count = 0
    for p in sorted(articles_dir.glob('*.txt')):
        try:
            title = p.stem
            text = p.read_text(encoding='utf-8', errors='ignore')
            insert_article(conn, title, text)
            count += 1
            if max_articles and count >= max_articles:
                break
        except Exception:
            continue
    conn.close()
    return count


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description='Convert wiki per-article txt files into sqlite DB')
    parser.add_argument('--outdir', default='data/wiki_dumps',
                        help='Base output dir where language folders are located')
    parser.add_argument('--lang', default='en', help='Language code')
    parser.add_argument('--max', type=int, default=0,
                        help='Limit number of articles (0 = all)')
    args = parser.parse_args(argv)

    lang = args.lang
    base = Path(args.outdir) / lang
    articles_dir = base / 'articles'
    if not articles_dir.exists():
        print(f'Articles directory not found: {articles_dir}')
        return 2

    db_path = base / 'wikipedia.db'
    max_articles = args.max or None
    print(
        f'Building sqlite DB at {db_path} from articles in {articles_dir}...')
    count = build_from_articles(articles_dir, db_path, max_articles)
    print(f'Inserted {count} articles into {db_path}')
    # also write a small metadata file
    meta = base / 'index.json'
    if meta.exists():
        try:
            data = json.loads(meta.read_text(encoding='utf-8'))
            # store total count
            meta.write_text(json.dumps(
                {'count': count, 'lang': lang}, ensure_ascii=False, indent=2), encoding='utf-8')
        except Exception:
            pass
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
