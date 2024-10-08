from flask import Flask
from app.routes import home
from app.routes import home, dashboard, api
from app.db import init_db
from app.utils import filters


def create_app():
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    # register routes
    app.register_blueprint(home) 
    app.register_blueprint(dashboard)
    app.register_blueprint(api)

    # initialize database
    init_db(app)

    
    return app