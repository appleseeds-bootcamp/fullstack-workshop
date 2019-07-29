import utils.db as db_utils


def is_logged_in(request):
    username = request.get_cookie("username")
    session_id = request.get_cookie("session_id")

    return db_utils.is_user_session_valid(username, session_id)


def verify_user_or_signup(username, password, response):
    if not db_utils.is_user_exists(username): # User does not exist - sign up
        db_utils.create_new_user(username, password)
        session_id = db_utils.update_user_session(username, password)
        response.set_cookie("session_id", session_id)
        response.set_cookie("username", username)
        return True
    else: # The user exists - Sign in
        if db_utils.is_valid_password(username, password):
            session_id = db_utils.update_user_session(username, password)
            response.set_cookie("session_id", session_id)
            response.set_cookie("username", username)
            return True

    return False
    

