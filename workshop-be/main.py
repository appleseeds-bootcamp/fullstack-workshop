from bottle import run
import api

if __name__ == "__main__":
    run(host="localhost", port=4000, debug=True, reloader=True)