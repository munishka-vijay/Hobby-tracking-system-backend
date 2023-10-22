from database import db

class Hobby(db.Model):
    __tablename__ = 'hobby'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    duration = db.Column(db.Integer, nullable=True)  # You can change the data type if needed

    # Define relationships with Tag and User tables
    tag = db.relationship('Tag', backref='hobbies')
    user = db.relationship('User', backref='hobbies')

    def __init__(self, name, tag_id, user_id, start_date, start_time, duration=None):
        self.name = name
        self.tag_id = tag_id
        self.user_id = user_id
        self.start_date = start_date
        self.start_time = start_time
        self.duration = duration
    
    def save(self):
        db.session.add(self)
        db.session.commit()