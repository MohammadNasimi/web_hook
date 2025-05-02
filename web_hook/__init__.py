from flask import Flask
from .notes.routes import notes_blueprint
from web_hook.exceptions import resource_not_found, resource_sever_error, resource_bad_request

def register_error_handlers(app):
    app.register_error_handler(404,resource_not_found)
    app.register_error_handler(500,resource_sever_error)
    app.register_error_handler(400,resource_bad_request)



app = Flask(__name__)


app.register_blueprint(notes_blueprint)
register_error_handlers(app)

app.config.from_object('config.developconfig')
