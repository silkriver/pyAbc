"""在线文章聚合展示"""
from flask import Flask, render_template
from datetime import datetime
import sqlite3
import time
import json
app = Flask(__name__)


@app.route("/")
def index():
    mintime = time.time() - 72 * 60 * 60
    conn = sqlite3.connect("data/result.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT result FROM resultdb_sciencenet WHERE updatetime>? \
            UNION SELECT result from resultdb_solidot WHERE updatetime>?",
        (mintime, mintime))
    result = cur.fetchall()
    rows = []
    for r in result:
        rows.append(json.loads(r[0]))
    rows.sort(key=lambda i: i["date"], reverse=True)
    return render_template("index.html", rows=rows)
