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
    query = "SELECT id, name FROM users WHERE name = '" + name + "'"
    rows = conn.execute(query).fetchall()
    return {"users": rows}
