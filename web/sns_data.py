import sqlite3
import time, os

# --- DBファイルの場所 ---
BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(BASE_DIR, 'data', 'data.db')

# --- DB接続 ---
def get_conn():
    return sqlite3.connect(DATA_FILE)

# --- 初期化（テーブル作成） ---
def init_db():
    conn = get_conn()
    cur = conn.cursor()

    # お気に入りテーブル
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fav (
        id TEXT,
        fav_id TEXT,
        PRIMARY KEY (id, fav_id)
    )
    """)

    # 投稿テーブル
    cur.execute("""
    CREATE TABLE IF NOT EXISTS text (
        id TEXT,
        text TEXT,
        time REAL
    )
    """)

    conn.commit()
    conn.close()

# 起動時に作成
init_db()

# ===============================
# お気に入り関連
# ===============================

def add_fav(id, fav_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT OR IGNORE INTO fav (id, fav_id) VALUES (?, ?)",
        (id, fav_id)
    )

    conn.commit()
    conn.close()


def is_fav(id, fav_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "SELECT 1 FROM fav WHERE id=? AND fav_id=?",
        (id, fav_id)
    )

    result = cur.fetchone()
    conn.close()
    return result is not None


def remove_fav(id, fav_id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM fav WHERE id=? AND fav_id=?",
        (id, fav_id)
    )

    conn.commit()
    conn.close()


def get_fav_list(id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "SELECT fav_id FROM fav WHERE id=?",
        (id,)
    )

    rows = cur.fetchall()
    conn.close()

    return [r[0] for r in rows]


# ===============================
# 投稿関連
# ===============================

def write_text(id, text):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO text (id, text, time) VALUES (?, ?, ?)",
        (id, text, time.time())
    )

    conn.commit()
    conn.close()


def get_text(id):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, text, time FROM text WHERE id=?",
        (id,)
    )

    rows = cur.fetchall()
    conn.close()

    return [
        {"id": r[0], "text": r[1], "time": r[2]}
        for r in rows
    ]


# ===============================
# タイムライン
# ===============================

def get_timelines(id):
    favs = get_fav_list(id)
    favs.append(id)

    tm = time.time() - (24 * 60 * 60) * 30  # 30日

    conn = get_conn()
    cur = conn.cursor()

    placeholders = ",".join("?" * len(favs))

    cur.execute(
        f"""
        SELECT id, text, time
        FROM text
        WHERE id IN ({placeholders})
        AND time >= ?
        ORDER BY time DESC
        """,
        (*favs, tm)
    )

    rows = cur.fetchall()
    conn.close()

    return [
        {"id": r[0], "text": r[1], "time": r[2]}
        for r in rows
    ]
