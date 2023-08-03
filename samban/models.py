from samban import db

class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant_id = db.Column(db.Integer, nullable=False, unique=True)
    create_date = db.Column(db.DateTime(), nullable=False)
    reply1 = db.Column(db.Text(), nullable=True)
    score = db.Column(db.Float, nullable=True)
    reply2 = db.Column(db.Text(), nullable=True)
    score2 = db.Column(db.Float, nullable=True)
    condition = db.Column(db.Integer, nullable=True)
    chatGPT = db.Column(db.Text(), nullable=True)



