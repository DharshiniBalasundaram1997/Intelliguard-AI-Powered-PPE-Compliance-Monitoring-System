import psycopg2
import os

from connect_rds_util import connect_to_postgres, connect_to_violation_logs_db
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def ensure_database_exists():
    try:
        conn = connect_to_postgres()
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        db_name = os.getenv("DB_NAME")
        cursor.execute("SELECT * FROM pg_database WHERE datname = %s", (db_name,))
        exists = cursor.fetchone()
        print(exists)

        if not exists:
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"✅ Database '{db_name}' created.")
        else:
            print(f"ℹ️  Database '{db_name}' already exists.")

        cursor.close()
        conn.close()
    except Exception as e:
        print("❌ Error checking/creating DB:", e)

def create_violation_logs_table():
    try:
        conn = connect_to_violation_logs_db()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS violation_logs_db (
                id SERIAL PRIMARY KEY,
                image_url TEXT NOT NULL,
                detected_items TEXT NOT NULL,
                no_of_violation_class TEXT NOT NULL,
                confidence TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        cursor.execute("""SELECT column_name, data_type FROM information_schema.columns 
                       WHERE table_name = 'violation_logs_db';""")
        result = cursor.fetchall()
        print(result)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ violation_logs table is ready.")
    except Exception as e:
        print("❌ Error creating table:", e)

if __name__ == "__main__":
    ensure_database_exists()
    create_violation_logs_table()
