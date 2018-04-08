from db.OpenConn import ConnManager
from db.sql import *

def initialize_tables():
    create_table(sql_create_stacks_table)
    create_table(sql_create_cards_table)
    create_table(sql_create_questions_table)
    create_table(sql_create_answers_table)
    create_table(sql_create_assets_table)


def create_table(sql):
    with ConnManager() as cursor:
        cursor.execute(sql)


# Stacks

def create_stack(name):
    with ConnManager() as cursor:
        cursor.execute(sql_insert_stack, (name,))
        return cursor.lastrowid


def delete_stack(stack_id):
    with ConnManager() as cursor:
        cursor.execute(sql_delete_stack, (stack_id,))
        cursor.execute(sql_delete_stack_cards, (stack_id,))


def get_stacks():
    with ConnManager() as cursor:
        cursor.execute("SELECT * FROM stacks")
        return cursor.fetchall()


# Cards

def create_card(stack_id):
    with ConnManager() as cursor:
        cursor.execute(sql_insert_card, (stack_id,))
        card_id = cursor.lastrowid

        cursor.execute(sql_insert_question, (card_id,))
        cursor.execute(sql_insert_answer, (card_id,))

        return card_id


def delete_card(card_id):
    with ConnManager() as cursor:
        cursor.execute(sql_delete_card, (card_id,))
        cursor.execute(sql_delete_card_questions, (card_id,))
        cursor.execute(sql_delete_card_answers, (card_id,))

def select_cards_by_stack_id(conn, stack_id):
    cur = conn.cursor()
    cur.execute("SELECT id FROM cards WHERE stack_id=?", (stack_id,))
    return cur.fetchall()

def get_stack_cards(stack_id):
    with ConnManager() as cursor:
        cursor.execute(sql_select_stack_cards, (stack_id,))
        return cursor.fetchall()

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

def create_asset(asset):
    with ConnManager() as cursor:
        cursor.execute(sql_insert_asset, asset)
        return cursor.lastrowid

def update_asset(conn, asset_id, content, filename):
    cur = conn.cursor()
    cur.execute(sql_update_asset, (content, filename, asset_id,))
    conn.commit()

def delete_asset(asset_id):
    with ConnManager() as cursor:
        cursor.execute(sql_delete_asset, (asset_id,))

def select_assets_by_card_id(conn, card_id):
    cur = conn.cursor()
    cur.execute(sql_select_assets_by_card_id, (card_id,))
    return cur.fetchall()
