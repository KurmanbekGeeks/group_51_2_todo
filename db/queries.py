CREATE_TABLE_TASKS = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        )
"""

SELECT_TASKS = "SELECT id, task FROM tasks"

INSERT_TASK = "INSERT INTO tasks (task) VALUES (?)"

UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"

DELETE_TASK = "DELETE FROM tasks WHERE id = ?"

