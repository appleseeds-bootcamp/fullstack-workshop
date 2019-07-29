import pymysql
import hashlib
from uuid import uuid4

_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    db="workshop",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def hash_password(password):
    salt = "13Ebu54"
    return hashlib.md5((salt + password).encode('utf-8')).hexdigest()

def get_user_session_id():
    return uuid4().hex[:8]

def create_new_user(user_name, password):
    hashed_password = hash_password(password)
    try:
        with _connection.cursor() as cursor:
            sql = f"INSERT INTO users(user_name, password) VALUES('{user_name}', '{hashed_password}')"
            print(sql)

            cursor.execute(sql)
            _connection.commit()
    except Exception as e:
        print(f"An error occured when trying to create new user, error: {e}")
        return False

    return True


def is_user_exists(user_name):
    try:
        with _connection.cursor() as cursor:
            sql = f"SELECT * FROM users WHERE user_name='{user_name}'"
            cursor.execute(sql)
            result = cursor.fetchone()

            return result is not None
    except Exception as e:
        print(f"An error occured when trying to fetch user, error: {e}")
        return False

def is_valid_password(user_name, password):
    hashed_password = hash_password(password)
    try:
        with _connection.cursor() as cursor:
            sql = f"SELECT * FROM users WHERE user_name='{user_name}' AND password='{hashed_password}'"

            cursor.execute(sql)
            result = cursor.fetchone()

            return result is not None
    except Exception as e:
        print(f"An error occured when trying to fetch user, error: {e}")
        return False

def update_user_session(user_name, password):
    hashed_password = hash_password(password)
    new_session_id = get_user_session_id()
    try:
        with _connection.cursor() as cursor:
            sql = f"UPDATE users SET session_id='{new_session_id}' WHERE user_name='{user_name}' AND password='{hashed_password}'"

            cursor.execute(sql)
            _connection.commit()
            return new_session_id
    except Exception as e:
        print(f"An error occured when trying to update user session, error: {e}")
        return False

def is_user_session_valid(user_name, session_id):
    try:
        with _connection.cursor() as cursor:
            sql = f"SELECT * from users WHERE session_id='{session_id}' AND user_name='{user_name}'"

            cursor.execute(sql)
            result = cursor.fetchone()
            return result is not None

    except Exception as e:
        print(f"An error occured when trying to update user session, error: {e}")
        return False