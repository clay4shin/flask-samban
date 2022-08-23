import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

naming_convention = {
    "ix": 'ix_%(column_0_labels)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate(compare_type=True)

def create_app():
    app = Flask(__name__)
    app.config.from_envvar('APP_CONFIG_FILE')

    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models

    # blueprint
    from .views import main_views, _1_nokids_neg_noscore_norev, _2_nokids_neg_noscore_rev, _3_nokids_neg_score_rev, _4_nokids_pos_noscore_norev, _5_nokids_pos_noscore_rev, _6_nokids_pos_score_rev
    app.register_blueprint(main_views.bp)
    app.register_blueprint(_1_nokids_neg_noscore_norev.bp)
    app.register_blueprint(_2_nokids_neg_noscore_rev.bp)
    app.register_blueprint(_3_nokids_neg_score_rev.bp)
    app.register_blueprint(_4_nokids_pos_noscore_norev.bp)
    app.register_blueprint(_5_nokids_pos_noscore_rev.bp)
    app.register_blueprint(_6_nokids_pos_score_rev.bp)

    return app
