from flask import Flask
import psycopg2
import traceback

from contextlib import contextmanager

from psycopg2.extras import NamedTupleCursor
from psycopg2.extras import execute_batch
from DBUtils.PersistentDB import PersistentDB

PERSISTENT_DB = PersistentDB(
    psycopg2,
    # No maximum number of connections
    None,
    user='postgres',
    password='postgres',
    host='db',
    port=5432,
    dbname='postgres'
)

@contextmanager
def context_db_cursor():
    try:
        db = PERSISTENT_DB.connection()
        cursor = db.cursor(cursor_factory=NamedTupleCursor)
    except Exception as e:  # pragma: no cover
        traceback.print_exc()

        # Close the old connection, then get a new one
        db.close()
        db = PERSISTENT_DB.steady_connection()
        cursor = db.cursor(cursor_factory=NamedTupleCursor)

    try:
        db.begin()
        yield (db, cursor)
        cursor.close()
        db.commit()
    except:  # pragma: no cover
        traceback.print_exc()
        db.rollback()

app = Flask(__name__)

@app.route('/')
def root():
    with context_db_cursor() as (db, cursor):
        cursor.execute("SELECT 1 AS pong;")
        try:
            return "<html><body><pre>OK {}</pre></body></html>".format(cursor.fetchone().pong)
        except:
            return "<html><body><pre>{}</pre></body></html>".format(traceback.format_exc()).replace("<", "&lt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
