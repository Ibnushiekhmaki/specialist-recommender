import sqlite3

DB_PATH = "specialists.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS specialists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS symptom_rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symptom_tag TEXT NOT NULL,
            specialist_id INTEGER NOT NULL,
            notes TEXT,
            FOREIGN KEY (specialist_id) REFERENCES specialists (id)
        )
    """)

    conn.commit()
    conn.close()
    print("Tables created successfully.")

if __name__ == "__main__":
    create_tables()