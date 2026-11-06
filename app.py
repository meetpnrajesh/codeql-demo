import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/users")
def users():
    name = request.args.get("name", "")
    conn = sqlite3.connect("app.db")
    rows = conn.execute("SELECT id, name FROM users WHERE name = ?", (name,)).fetchall()
    return {"users": rows}
