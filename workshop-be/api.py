"""
Available endpoints:
GET: /
GET/POST: /login

Static files routes
"""
from bottle import template, get, post, static_file, redirect, request, response
import utils.login as login_utils

FE_STATIC_FILES_PATH = "../workshop-fe/build"


# Static files:
@get('/static/<dirname>/<filename>')
def serve_static_dir(dirname, filename):
    return static_file(filename, root=f'{FE_STATIC_FILES_PATH}/static/{dirname}')

@get("/<filename>")
def serve_root_dir(filename):
    if filename == "index.html": # We want to avoid getting /index.html directly.
        redirect("/")
    return static_file(filename, root=FE_STATIC_FILES_PATH)

@get("/")
def index():
    if login_utils.is_logged_in(request):
        return static_file("index.html", root=FE_STATIC_FILES_PATH)
    
    return redirect("/login?next_url=/")

@get("/login")
def serve_login_page():
    if login_utils.is_logged_in(request):
        return redirect("/")
    
    next_url = request.GET.get("next_url","/")
    return template("templates/login.html", next_url=next_url, err_msg="")
