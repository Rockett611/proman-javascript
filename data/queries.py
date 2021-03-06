from data import data_manager


def get_boards():
    return data_manager.execute_select('SELECT * FROM boards;')


def get_columns_to_board(board_id):
    return data_manager.execute_select("SELECT title FROM columns WHERE boardID=%(relatedBoard)s",
                                       {'relatedBoard': board_id})


def get_tasks_to_board_and_column(board_id):
    return data_manager.execute_select("SELECT taskID, columnID, title, content FROM tasks "
                                       "WHERE boardID=%(relatedBoard)s ",
                                       {'relatedBoard': board_id})


def get_pass_by_email(email):
    return data_manager.execute_select(" SELECT password FROM users WHERE "
                                       "email=%(email)s;",
                                       {'email': email})


def add_board(board_data):
    return data_manager.execute_dml_statement("INSERT INTO boards (title, userID) "
                                              "VALUES(%(title)s, %(user_id)s);", board_data)


def add_column(column):
    return data_manager.execute_dml_statement("INSERT INTO columns (title, boardID) "
                                              "VALUES(%(title)s, %(board_id)s);", column)


def add_user(user_data):
    return data_manager.execute_dml_statement("INSERT INTO users (email, username, password)"
                                              "VALUES %(email)s, %(username)s, %(password)s);", user_data)


def change_task_column(task_id, new_col):
    return data_manager.execute_dml_statement("UPDATE tasks "
                                            " SET columnid = %(new_column)s "
                                            " WHERE taskid=%(task_id)s;",
                                            {'task_id': task_id, 'new_column': new_col})
