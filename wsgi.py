import os
from bottle import static_file, Bottle, run
APP_ROOT = os.path.dirname(__file__)
STATIC_ROOT = os.path.join(APP_ROOT, "static")

application = Bottle()

@application.route('/static/<filename:path>')
def serve_static(filename):
    return static_file(filename, root=STATIC_ROOT)

@application.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    run(application)