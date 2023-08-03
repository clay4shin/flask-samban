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
    # below for the very first study - comment them out when not necessary
    from .views import main_views, \
        _1_nokids_neg_noscore_norev, _2_nokids_neg_noscore_rev, _3_nokids_neg_score_rev, _4_nokids_pos_noscore_norev, \
        _5_nokids_pos_noscore_rev, _6_nokids_pos_score_rev
    # app.register_blueprint(main_views.bp)
    # app.register_blueprint(_1_nokids_neg_noscore_norev.bp)
    # app.register_blueprint(_2_nokids_neg_noscore_rev.bp)
    # app.register_blueprint(_3_nokids_neg_score_rev.bp)
    # app.register_blueprint(_4_nokids_pos_noscore_norev.bp)
    # app.register_blueprint(_5_nokids_pos_noscore_rev.bp)
    # app.register_blueprint(_6_nokids_pos_score_rev.bp)
    from .views.y2s1 import _1_gun_neg_maj_high_noscore, _2_gun_neg_maj_high_score, _3_gun_neg_maj_high_scorechat, \
        _4_gun_neg_maj_low_noscore, _5_gun_neg_maj_low_score, _6_gun_neg_maj_low_scorechat, _7_gun_neg_min_high_noscore, \
        _8_gun_neg_min_high_score, _9_gun_neg_min_high_scorechat, _10_gun_neg_min_low_noscore, _11_gun_neg_min_low_score, \
        _12_gun_neg_min_low_scorechat, _13_gun_pos_maj_high_noscore, _14_gun_pos_maj_high_score, _15_gun_pos_maj_high_scorechat, \
        _16_gun_pos_maj_low_noscore, _17_gun_pos_maj_low_score, _18_gun_pos_maj_low_scorechat, _19_gun_pos_min_high_noscore, \
        _20_gun_pos_min_high_score, _21_gun_pos_min_high_scorechat, _22_gun_pos_min_low_noscore, _23_gun_pos_min_low_score, \
        _24_gun_pos_min_low_scorechat, _25_race_neg_maj_high_noscore, _26_race_neg_maj_high_score, _27_race_neg_maj_high_scorechat,\
        _28_race_neg_maj_low_noscore, _29_race_neg_maj_low_score, _30_race_neg_maj_low_scorechat, _31_race_neg_min_high_noscore, \
        _32_race_neg_min_high_score, _33_race_neg_min_high_scorechat, _34_race_neg_min_low_noscore, _35_race_neg_min_low_score, \
        _36_race_neg_min_low_scorechat, _37_race_pos_maj_high_noscore, _38_race_pos_maj_high_score, _39_race_pos_maj_high_scorechat, \
        _40_race_pos_maj_low_noscore, _41_race_pos_maj_low_score, _42_race_pos_maj_low_scorechat, _43_race_pos_min_high_noscore, \
        _44_race_pos_min_high_score, _45_race_pos_min_high_scorechat, _46_race_pos_min_low_noscore, _47_race_pos_min_low_score, \
        _48_race_pos_min_low_scorechat
    app.register_blueprint(_1_gun_neg_maj_high_noscore.bp)
    app.register_blueprint(_2_gun_neg_maj_high_score.bp)
    app.register_blueprint(_3_gun_neg_maj_high_scorechat.bp)
    app.register_blueprint(_4_gun_neg_maj_low_noscore.bp)
    app.register_blueprint(_5_gun_neg_maj_low_score.bp)
    app.register_blueprint(_6_gun_neg_maj_low_scorechat.bp)
    app.register_blueprint(_7_gun_neg_min_high_noscore.bp)
    app.register_blueprint(_8_gun_neg_min_high_score.bp)
    app.register_blueprint(_9_gun_neg_min_high_scorechat.bp)
    app.register_blueprint(_10_gun_neg_min_low_noscore.bp)
    app.register_blueprint(_11_gun_neg_min_low_score.bp)
    app.register_blueprint(_12_gun_neg_min_low_scorechat.bp)
    app.register_blueprint(_13_gun_pos_maj_high_noscore.bp)
    app.register_blueprint(_14_gun_pos_maj_high_score.bp)
    app.register_blueprint(_15_gun_pos_maj_high_scorechat.bp)
    app.register_blueprint(_16_gun_pos_maj_low_noscore.bp)
    app.register_blueprint(_17_gun_pos_maj_low_score.bp)
    app.register_blueprint(_18_gun_pos_maj_low_scorechat.bp)
    app.register_blueprint(_19_gun_pos_min_high_noscore.bp)
    app.register_blueprint(_20_gun_pos_min_high_score.bp)
    app.register_blueprint(_21_gun_pos_min_high_scorechat.bp)
    app.register_blueprint(_22_gun_pos_min_low_noscore.bp)
    app.register_blueprint(_23_gun_pos_min_low_score.bp)
    app.register_blueprint(_24_gun_pos_min_low_scorechat.bp)
    app.register_blueprint(_25_race_neg_maj_high_noscore.bp)
    app.register_blueprint(_26_race_neg_maj_high_score.bp)
    app.register_blueprint(_27_race_neg_maj_high_scorechat.bp)
    app.register_blueprint(_28_race_neg_maj_low_noscore.bp)
    app.register_blueprint(_29_race_neg_maj_low_score.bp)
    app.register_blueprint(_30_race_neg_maj_low_scorechat.bp)
    app.register_blueprint(_31_race_neg_min_high_noscore.bp)
    app.register_blueprint(_32_race_neg_min_high_score.bp)
    app.register_blueprint(_33_race_neg_min_high_scorechat.bp)
    app.register_blueprint(_34_race_neg_min_low_noscore.bp)
    app.register_blueprint(_35_race_neg_min_low_score.bp)
    app.register_blueprint(_36_race_neg_min_low_scorechat.bp)
    app.register_blueprint(_37_race_pos_maj_high_noscore.bp)
    app.register_blueprint(_38_race_pos_maj_high_score.bp)
    app.register_blueprint(_39_race_pos_maj_high_scorechat.bp)
    app.register_blueprint(_40_race_pos_maj_low_noscore.bp)
    app.register_blueprint(_41_race_pos_maj_low_score.bp)
    app.register_blueprint(_42_race_pos_maj_low_scorechat.bp)
    app.register_blueprint(_43_race_pos_min_high_noscore.bp)
    app.register_blueprint(_44_race_pos_min_high_score.bp)
    app.register_blueprint(_45_race_pos_min_high_scorechat.bp)
    app.register_blueprint(_46_race_pos_min_low_noscore.bp)
    app.register_blueprint(_47_race_pos_min_low_score.bp)
    app.register_blueprint(_48_race_pos_min_low_scorechat.bp)

    return app
