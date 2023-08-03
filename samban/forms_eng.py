from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

class IDForm(FlaskForm):
    ID = StringField('Participant ID', validators=[InputRequired('Participant ID is required to proceed.')])

class Reply1Form(FlaskForm):
    Reply1 = TextAreaField('Please write your comment.', validators=[InputRequired('Your comment is required to proceed.')])

class Reply2Form(FlaskForm):
    Reply2 = TextAreaField('Please write your comment.', validators=[InputRequired('Your comment is required to proceed.')])