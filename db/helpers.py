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
    create_table(conn, sql_create_questions_table)
    create_table(conn, sql_create_answers_table)
    create_table(conn, sql_create_assets_table)


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


# Stacks

def create_stack(conn, name):
    cur = conn.cursor()
    cur.execute(sql_insert_stack, (name,))
    conn.commit()
    return cur.lastrowid


def delete_stack(conn, stack_id):
    cur = conn.cursor()
    cur.execute(sql_delete_stack, (stack_id,))
    conn.commit()


def select_all_stacks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM stacks")
    return cur.fetchall()


# Cards

def create_card(conn, stack_id):
    cur = conn.cursor()
    cur.execute(sql_insert_card, (stack_id,))
    card_id = cur.lastrowid

    cur.execute(sql_insert_question, (card_id,))
    cur.execute(sql_insert_answer, (card_id,))
    conn.commit()

    return card_id
