import sqlite3
from sqlite3 import Error
from db.schema import *

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def initialize_tables(conn):
    create_table(conn, sql_create_stacks_table)
    create_table(conn, sql_create_cards_table)


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_stack(conn, stack):
    cur = conn.cursor()
    cur.execute(sql_insert_stack, stack)
    conn.commit()
    return cur.lastrowid


def select_all_stacks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM stacks")

    rows = cur.fetchall()

    for row in rows:
        print(row)
