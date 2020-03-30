"""在线文章聚合展示"""
from flask import Flask, render_template
from datetime import datetime
from flask_paginate import Pagination, get_page_args
import sqlite3
import time
import json
app = Flask(__name__)


def get_rows(rows, offset=0, per_page=10):
    return rows[offset:offset + per_page]


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
    page, per_page, offset = get_page_args(
        page_parameter="page", per_page_parameter="per_page")
    pagination_rows = get_rows(rows=rows, offset=offset, per_page=per_page)
    pagination = Pagination(
        page=page, per_page=per_page, total=len(rows),
        css_framework="bootstrap4")
    return render_template(
        "index.html", rows=pagination_rows,
        page=page, per_page=per_page, pagination=pagination)
