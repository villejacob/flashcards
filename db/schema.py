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
        FOREIGN KEY (stack_id) REFERENCES stacks (id)
    ); '''

sql_insert_stack = '''
    INSERT INTO stacks(name, last_reviewed)
    VALUES(?,?)
    '''
