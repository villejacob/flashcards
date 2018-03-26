# Create tables

sql_create_stacks_table = '''
    CREATE TABLE IF NOT EXISTS stacks (
        id integer PRIMARY KEY,
        name text NOT NULL,
        last_reviewed text
    ); '''

sql_create_cards_table = '''
    CREATE TABLE IF NOT EXISTS cards (
        id integer PRIMARY KEY,
        stack_id integer NOT NULL,
        FOREIGN KEY (stack_id) REFERENCES stacks(id)
    ); '''

sql_create_questions_table = '''
    CREATE TABLE IF NOT EXISTS questions (
        id integer PRIMARY KEY,
        card_id integer NOT NULL,
        FOREIGN KEY (card_id) REFERENCES cards (id)
    ); '''

sql_create_answers_table = '''
    CREATE TABLE IF NOT EXISTS answers (
        id integer PRIMARY KEY,
        card_id integer NOT NULL,
        FOREIGN KEY (card_id) REFERENCES cards (id)
    ); '''

sql_create_assets_table = '''
    CREATE TABLE IF NOT EXISTS assets (
        id integer PRIMARY KEY,
        question_id integer,
        answer_id integer,
        type text NOT NULL,
        content text,
        filename text,
        left real NOT NULL,
        top real NOT NULL,
        width real,
        height real,
        FOREIGN KEY (question_id) REFERENCES questions (id),
        FOREIGN KEY (answer_id) REFERENCES answers (id)
    ); '''


# Stacks

sql_insert_stack = '''
    INSERT INTO stacks(name, last_reviewed)
    VALUES(?,NULL)
    '''

sql_delete_stack = '''
    DELETE FROM stacks WHERE id=?
    '''


# Cards

sql_insert_card = '''
    INSERT INTO cards(stack_id)
    VALUES(?)
    '''

sql_delete_card = '''
    DELETE FROM cards WHERE id=?
    '''

sql_delete_card_by_stack_id = '''
    DELETE FROM cards WHERE stack_id=?
    '''


# Questions

sql_insert_question = '''
    INSERT INTO questions(card_id)
    VALUES(?)
    '''

sql_delete_question_by_card_id = '''
    DELETE FROM questions WHERE card_id=?
    '''


# Answers

sql_insert_answer = '''
    INSERT INTO answers(card_id)
    VALUES(?)
    '''

sql_delete_answer_by_card_id = '''
    DELETE FROM answers WHERE card_id=?
    '''


# Assets

sql_insert_asset = '''
    INSERT INTO assets(question_id, answer_id, type, content, filename, left,
    top, width, height)
    VALUES(?,?,?,?,?,?,?,?,?)
    '''

sql_delete_asset = '''
    DELETE FROM assets WHERE id=?
    '''