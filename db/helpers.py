import sqlite3
from sqlite3 import Error
from db.schema import *

def create_connection(db_file):
    try:
        return sqlite3.connect(db_file)
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
        cur = conn.cursor()
        cur.execute(create_table_sql)
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
    cur.execute(sql_delete_card_by_stack_id, (stack_id,))
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


def delete_card(conn, card_id):
    cur = conn.cursor()
    cur.execute(sql_delete_card, (card_id,))
    cur.execute(sql_delete_question_by_card_id, (card_id,))
    cur.execute(sql_delete_answer_by_card_id, (card_id,))
    conn.commit()

# Questions

def select_question_by_card_id(conn, card_id):
    cur = conn.cursor()
    cur.execute("SELECT id FROM questions WHERE card_id=?", (card_id,))
    return cur.fetchone()[0]

# Answers

def select_answer_by_card_id(conn, card_id):
    cur = conn.cursor()
    cur.execute("SELECT id FROM answers WHERE card_id=?", (card_id,))
    return cur.fetchone()[0]

# Assets

def create_asset(conn, asset):
    cur = conn.cursor()
    cur.execute(sql_insert_asset, asset)
    conn.commit()
    return cur.lastrowid

def update_asset(conn, asset_id, content, filename):
    cur = conn.cursor()
    cur.execute(sql_update_asset, (content, filename, asset_id,))
    conn.commit()

def delete_asset(conn, asset_id):
    cur = conn.cursor()
    cur.execute(sql_delete_asset, (asset_id,))
    conn.commit()

def select_assets_by_card_id(conn, card_id):
    cur = conn.cursor()
    cur.execute(sql_select_assets_by_card_id, (card_id,))
    return cur.fetchall()
