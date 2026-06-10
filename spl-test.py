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
