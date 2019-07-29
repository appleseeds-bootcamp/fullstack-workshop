def is_logged_in(request):
    username = request.get_cookie("username")
    session_id = request.get_cookie("session_id")
    return False

def verify_user():
    pass