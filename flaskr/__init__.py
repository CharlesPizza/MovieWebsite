import os
from flask import Flask 

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/test')
    def test():
        return 'Testing...'


    # Importing db.py from local directory and initializing the db with
    # teardown context and an added command within context of 'app'
    from . import db
    db.init_app(app)
    # Importing auth blueprint
    from . import auth
    app.register_blueprint(auth.bp)
    from . import temp 
    app.register_blueprint(temp.bp)
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    from . import movies
    app.register_blueprint(movies.bp)

    return app