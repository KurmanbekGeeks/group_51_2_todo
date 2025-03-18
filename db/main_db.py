import sqlite3
from config import DB_PATH
from db import queries


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_TASKS)
    conn.commit()
    conn.close()


def get_tasks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_TASKS)
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def add_task_db(task):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_TASK, (task,))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id


def update_task_db(task_id, new_task):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_TASK, (new_task, task_id))
    conn.commit()
    conn.close()


def delete_task_db(task_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (task_id,))
    conn.commit()
    conn.close()

    