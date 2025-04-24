import sqlite3
from datetime import datetime, date
from config import DB_PATH
from db import queries


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_TASKS)
    conn.commit()
    conn.close()


def get_tasks(filter_type="all"):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if filter_type == 'completed':
        cursor.execute(queries.SELECT_completed)
    elif filter_type == "incomplete":
        cursor.execute(queries.SELECT_incomplete)
    elif filter_type == "deadline":
        cursor.execute(queries.SELECT_BY_DEADLINE)
    else:
        cursor.execute(queries.SELECT_TASKS)

    tasks = cursor.fetchall()
    conn.close()
    return tasks


def add_task_db(task, deadline=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_TASK, (task, deadline))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id


# def update_task_db(task_id, new_task):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute(queries.UPDATE_TASK, (new_task, task_id))
#     conn.commit()
#     conn.close()


def update_task_db(task_id, new_task=None, completed=None, deadline=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if new_task is not None:
        cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_task, task_id))
    if completed is not None:
        cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (completed, task_id))
    if deadline is not None:
        cursor.execute(queries.UPDATE_DEADLINE, (deadline, task_id))

    conn.commit()
    conn.close()

def delete_task_db(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (task_id,))
    conn.commit()
    conn.close()

def get_upcoming_deadlines():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_BY_DEADLINE)
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# pip install flet[all]