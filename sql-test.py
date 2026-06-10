Last login: Tue Jun  9 13:35:49 on ttys000
h.okamura@CSC-R244 ~ % ls
code
Desktop
dev
development
Documents
Downloads
git-sample
git-training
git-training02
git-training04
Library
Movies
Music
next
nextjs-postgres-nextauth-tailwindcss-template
nodenv
Pictures
prod-ca-2021.crt
progate_path
Public
sample

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
-- INSERT --
        conn.executemany(
      --panel: #ffffff;
      --ink: #18202a;
      --muted: #667085;
      --line: #d7dde4;
      --accent: #2364aa;
      --danger: #b42318;
      --ok: #027a48;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      background: var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    main {{
      width: min(920px, calc(100vw - 32px));
      display: grid;
      grid-template-columns: minmax(280px, 380px) 1fr;
      gap: 24px;
      align-items: start;
-- INSERT (paste) --
      grid-template-columns: minmax(280px, 380px) 1fr;
supabase_schema.sql
worktree-practice
h.okamura@CSC-R244 ~ % cd
h.okamura@CSC-R244 ~ % mkdir git-sql-test
h.okamura@CSC-R244 ~ % cd git-sql-test
h.okamura@CSC-R244 git-sql-test % git init
Initialized empty Git repository in /Users/h.okamura/git-sql-test/.git/
h.okamura@CSC-R244 git-sql-test % git remotee
git: 'remotee' is not a git command. See 'git --help'.

The most similar commands are
	remote
	remote-ext
h.okamura@CSC-R244 git-sql-test % git remote
h.okamura@CSC-R244 git-sql-test % git remote add origin https://github.com/Haruto-csc/sql-test.git
h.okamura@CSC-R244 git-sql-test % git remote -vvv
origin	https://github.com/Haruto-csc/sql-test.git (fetch)
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from http.cookies import SimpleCookie
from urllib.parse import parse_qs
import html
import sqlite3


HOST = "127.0.0.1"
PORT = 8080
DB_PATH = "demo_users.sqlite3"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                display_name TEXT NOT NULL
            )
            """
"spl-test.py" 100L, 2640B
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from http.cookies import SimpleCookie
from urllib.parse import parse_qs


HOST = "0.0.0.0"
PORT = 8080
DB_PATH = "demo_users.sqlite3"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                display_name TEXT NOT NULL
            )
            """
        )
        conn.execute("DELETE FROM users")
        conn.executemany(
            [
                ("admin", "admin123", "管理者"),
                ("alice", "wonderland", "Alice"),
                ("bob", "builder", "Bob"),
            ],
        )
        conn.commit()
    finally:
        conn.close()


def page(message="", query="", username="", status=""):
    escaped_message = html.escape(message)
    escaped_query = html.escape(query)
    escaped_username = html.escape(username)
    status_class = html.escape(status or "neutral")

    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SQL Injection Demo Login</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f4f6f8;
      --panel: #ffffff;
      --ink: #18202a;
      --muted: #667085;
      --line: #d7dde4;
      --accent: #2364aa;
      --danger: #b42318;
      --ok: #027a48;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      background: var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    main {{
      width: min(920px, calc(100vw - 32px));
      display: grid;
from http.cookies import SimpleCookie
origin	https://github.com/Haruto-csc/sql-test.git (push)
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from http.cookies import SimpleCookie
from urllib.parse import parse_qs
import html
import sqlite3


HOST = "0.0.0.0"
PORT = 8080
DB_PATH = "demo_users.sqlite3"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                display_name TEXT NOT NULL
            )
            """
"spl-test.py" 100L, 2638B
h.okamura@CSC-R244 git-sql-test % git remote -vv
origin	https://github.com/Haruto-csc/sql-test.git (fetch)

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
-- INSERT --
# 1. 軽量なPythonの環境をベースにする
origin	https://github.com/Haruto-csc/sql-test.git (push)
h.okamura@CSC-R244 git-sql-test % touch spl-test.py

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
-- INSERT --
version: '3.8'
h.okamura@CSC-R244 git-sql-test % vim spl-test.py
h.okamura@CSC-R244 git-sql-test % git add .
h.okamura@CSC-R244 git-sql-test % git commit -m "first"
[main (root-commit) 795b06e] first
 1 file changed, 100 insertions(+)
 create mode 100644 spl-test.py
h.okamura@CSC-R244 git-sql-test % git branch
* main
h.okamura@CSC-R244 git-sql-test % git push -u origin main
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 14 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 1.39 KiB | 1.39 MiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Haruto-csc/sql-test.git
 * [new branch]      main -> main
# 1. 軽量なPythonの環境をベースにする
FROM python:3.11-slim

# 2. コンテナ内の作業フォルダを /app に設定
WORKDIR /app

# 3. あなたのPythonプログラム（app.py）をコンテナ内にコピー
COPY app.py .

# 4. アプリが使うポート（8080）を開放
EXPOSE 8080

# 5. コンテナ起動時にプログラムを実行
CMD ["python", "app.py"]
~
~
~
~
~
~
~
~
~
~
"Dockerfile" 14L, 388B
branch 'main' set up to track 'origin/main'.
# 1. 軽量なPythonの環境をベースにする
FROM python:3.11-slim

# 2. コンテナ内の作業フォルダを /app に設定
WORKDIR /app

# 3. あなたのPythonプログラム（app.py）をコンテナ内にコピー
COPY app.py .

# 4. アプリが使うポート（8080）を開放
EXPOSE 8080

# 5. コンテナ起動時にプログラムを実行
CMD ["python", "app.py"]
~
~
~
~
~
~
~
~
~
~
-- INSERT --
# 1. 軽量なPythonの環境をベースにする
h.okamura@CSC-R244 git-sql-test % vim spl-test.py
h.okamura@CSC-R244 git-sql-test % vim spl-test.py
h.okamura@CSC-R244 git-sql-test % touch Dockerfile
h.okamura@CSC-R244 git-sql-test % vim Dockerfile
h.okamura@CSC-R244 git-sql-test % touch docker-compose.yml
h.okamura@CSC-R244 git-sql-test % vim docker-compose.yml
h.okamura@CSC-R244 git-sql-test % git add .
h.okamura@CSC-R244 git-sql-test % git commit -m "add Dockerfile and yml"
[main aeb5c6c] add Dockerfile and yml
 3 files changed, 24 insertions(+), 1 deletion(-)
 create mode 100644 Dockerfile
 create mode 100644 docker-compose.yml
h.okamura@CSC-R244 git-sql-test % git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 14 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 930 bytes | 930.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
# 1. 軽量なPythonの環境をベースにする
FROM python:3.11-slim

# 2. コンテナ内の作業フォルダを /app に設定
WORKDIR /app

# 3. あなたのPythonプログラム（app.py）をコンテナ内にコピー
COPY sql-test.py .

# 4. アプリが使うポート（8080）を開放
EXPOSE 8080

# 5. コンテナ起動時にプログラムを実行
CMD ["python", "app.py"]
~
~
~
~
~
~
~
~
~
~
-- INSERT --
# 1. 軽量なPythonの環境をベースにする
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Haruto-csc/sql-test.git
   795b06e..aeb5c6c  main -> main
h.okamura@CSC-R244 git-sql-test % vim Dockerfile
h.okamura@CSC-R244 git-sql-test % vim Dockerfile
h.okamura@CSC-R244 git-sql-test % mv spl-test.py sql-test.py
h.okamura@CSC-R244 git-sql-test % ls
docker-compose.yml	Dockerfile		sql-test.py
h.okamura@CSC-R244 git-sql-test % git add .
h.okamura@CSC-R244 git-sql-test % git commit -m "edit file name"
[main a897e26] edit file name
 2 files changed, 1 insertion(+), 1 deletion(-)
 rename spl-test.py => sql-test.py (100%)
h.okamura@CSC-R244 git-sql-test % git push
Enumerating objects: 5, done.
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from http.cookies import SimpleCookie
from urllib.parse import parse_qs
import html
import sqlite3


HOST = "0.0.0.0"
PORT = 8080
DB_PATH = "demo_users.sqlite3"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                display_name TEXT NOT NULL
            )
            """
-- INSERT --
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from http.cookies import SimpleCookie
from urllib.parse import parse_qs
import html
import sqlite3


HOST = "0.0.0.0"
PORT = 8080
DB_PATH = "demo_users.sqlite3"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                display_name TEXT NOT NULL
            )
            """
-- INSERT --from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from http.cookies import SimpleCookie
from urllib.parse import parse_qs
import html
import sqlite3


HOST = "0.0.0.0"
PORT = 8080
DB_PATH = "demo_users.sqlite3"


def init_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                display_name TEXT NOT NULL
            )
            """
        )
        conn.execute("DELETE FROM users")
        conn.executemany(
            "INSERT INTO users (username, password, display_name) VALUES (?, ?, ?)",
            [
                ("admin", "admin123", "管理者"),
                ("alice", "wonderland", "Alice"),
                ("bob", "builder", "Bob"),
            ],
        )
        conn.commit()
    finally:
        conn.close()


def page(message="", query="", username="", status=""):
    escaped_message = html.escape(message)
    escaped_query = html.escape(query)
    escaped_username = html.escape(username)
    status_class = html.escape(status or "neutral")

    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SQL Injection Demo Login</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f4f6f8;
      --panel: #ffffff;
      --ink: #18202a;
      --muted: #667085;
      --line: #d7dde4;
      --accent: #2364aa;
      --danger: #b42318;
      --ok: #027a48;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      background: var(--bg);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    main {{
      width: min(920px, calc(100vw - 32px));
      display: grid;
      grid-template-columns: minmax(280px, 380px) 1fr;
      gap: 24px;
      align-items: start;
    }}
    section, aside {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: 0 16px 40px rgba(24, 32, 42, 0.08);
    }}
    section {{ padding: 28px; }}
    aside {{ padding: 22px; }}
    h1 {{
      margin: 0 0 8px;
      font-size: 26px;
      line-height: 1.2;
      letter-spacing: 0;
    }}
    h2 {{
      margin: 0 0 12px;
      font-size: 18px;
      letter-spacing: 0;
    }}
    p {{ margin: 0 0 18px; color: var(--muted); line-height: 1.6; }}
