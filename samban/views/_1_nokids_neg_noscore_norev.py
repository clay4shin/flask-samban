from flask import Blueprint, render_template, url_for, request, flash, current_app
from werkzeug.utils import redirect
from datetime import datetime
from google.cloud import language_v1

from samban import db
from samban.models import Reply

from samban.forms import IDForm, Reply1Form, Reply2Form

bp = Blueprint('cond1', __name__, url_prefix='/cond1')

@bp.route('/', methods=('GET', 'POST'))
def index():
    current_app.logger.info("INFO 레벨로 출력")
    form = IDForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = Reply.query.filter_by(participant_id=form.ID.data).first()
        if user:
            flash("중복된 참여자 ID입니다. 본인의 참여자 ID를 재확인 후 다시 기입해 주세요.")
        else:
            r = Reply(participant_id=form.ID.data, create_date=datetime.now(), condition=1)
            db.session.add(r)
            db.session.commit()
            return redirect(url_for('cond1.direct', participant_id=form.ID.data))
    return render_template('index.html', form=form)

@bp.route('/direct/<int:participant_id>/', methods=('GET', 'POST'))
def direct(participant_id):
    form = Reply1Form()
    if request.method == 'POST' and form.validate_on_submit():
        q1 = Reply.query.filter(Reply.participant_id == participant_id)
        # reply 1 DB에 저장
        q1.update({'reply1': form.Reply1.data})
        # Google Cloud Client Library 시작 (korean specific)
        client = language_v1.LanguageServiceClient()
        for row in q1:
            document = language_v1.Document(content=row.reply1, type_=language_v1.Document.Type.PLAIN_TEXT,
                                            language='ko')
            sentiment = client.analyze_sentiment(
                request={"document": document}
            ).document_sentiment
            # sentiment analysis score DB에 저장
            q1.update({'score': sentiment.score})
            db.session.commit()
            return redirect(url_for('cond1.bye', participant_id=participant_id))
    return render_template('exposure_nokids_neg.html', participant_id=participant_id, form=form)

@bp.route('/direct/<int:participant_id>/result/bye', methods=('GET', 'POST'))
def bye(participant_id):
    return render_template('bye.html', participant_id=participant_id)

