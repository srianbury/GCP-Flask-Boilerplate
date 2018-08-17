import logging
from flask import Flask, redirect, request, session, url_for

def create_app(config, debug=True, testing=False, config_overrides=None):
    app = Flask(__name__)
    app.config.from_object(config)

    app.debug = debug
    app.testing = testing

    if config_overrides:
        app.config.update(config_overrides)

    #configure logging
    if not app.testing:
        logging.basicConfig(level=logging.INFO)

    #Register the grading CRUD blueprint
    from .crud import crud #TODO
    app.register_blueprint(crud)

    #add a default root route
    @app.route("/")
    def index():
        return redirect(url_for('crud.home'))

    #add an error handler.  this is useful for debugging the live application
    #however, you should disable the output of the exception for production
    #applications
    @app.errorhandler(500)
    def server_error(e):
        return """
        An internal error occured: <pre>{}</pre>
        See logs for full stacktrace.
        """.format(e), 500

    return app

