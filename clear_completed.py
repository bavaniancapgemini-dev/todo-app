import sqlite3


def clear_completed():

    conn = sqlite3.connect("todo.db")

    cursor = conn.cursor()

    cursor.execute(

        "DELETE FROM tasks WHERE status='Completed'"

    )

    conn.commit()

    conn.close()

    print("Completed Tasks Cleared")