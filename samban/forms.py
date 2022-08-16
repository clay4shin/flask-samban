from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

class IDForm(FlaskForm):
    ID = StringField('참여자 ID', validators=[InputRequired('ID는 필수입력 항목입니다.')])

class Reply1Form(FlaskForm):
    Reply1 = TextAreaField('당신의 댓글을 달아주세요.', validators=[InputRequired('댓글은 필수입력 항목입니다.')])

class Reply2Form(FlaskForm):
    Reply2 = TextAreaField('당신의 댓글을 달아주세요.', validators=[InputRequired('댓글은 필수입력 항목입니다.')])