import sqlite3


conn = sqlite3.connect("todo.db")

cursor = conn.cursor()


# USERS TABLE
cursor.execute("""

CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE,

    password TEXT

)

""")


# TASKS TABLE
cursor.execute("""

CREATE TABLE IF NOT EXISTS tasks (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    task TEXT,

    status TEXT,

    priority TEXT,

    category TEXT,

    created TEXT,

    due TEXT

)

""")

conn.commit()


# =========================
# USER FUNCTIONS
# =========================

def register_user(username, password):

    try:

        cursor.execute(

            "INSERT INTO users (username, password) VALUES (?, ?)",

            (username, password)

        )

        conn.commit()

        return True

    except:

        return False


def login_user(username, password):

    cursor.execute(

        "SELECT * FROM users WHERE username=? AND password=?",

        (username, password)

    )

    return cursor.fetchone()


# =========================
# TASK FUNCTIONS
# =========================

def add_task(username, task, status, priority, category, created, due):

    cursor.execute(

        """

        INSERT INTO tasks

        (username, task, status, priority, category, created, due)

        VALUES (?, ?, ?, ?, ?, ?, ?)

        """,

        (username, task, status, priority, category, created, due)

    )

    conn.commit()


def load_tasks(username):

    cursor.execute(

        "SELECT * FROM tasks WHERE username=?",

        (username,)

    )

    return cursor.fetchall()


def delete_task(task_id):

    cursor.execute(

        "DELETE FROM tasks WHERE id=?",

        (task_id,)

    )

    conn.commit()


def update_task(task_id, task, priority, category, due):

    cursor.execute(

        """

        UPDATE tasks

        SET task=?, priority=?, category=?, due=?

        WHERE id=?

        """,

        (task, priority, category, due, task_id)

    )

    conn.commit()


def complete_task(task_id):

    cursor.execute(

        """

        UPDATE tasks

        SET status='Completed'

        WHERE id=?

        """,

        (task_id,)

    )

    conn.commit()