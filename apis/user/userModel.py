from database import db

class User (db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(500), unique=False, nullable=False)
    role = db.Column(db.String(10), default='user', nullable = False)

    def __init__(self, username, email, phone, password, role):
        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
        self.role=role
    
    def save(self):
        db.session.add(self)
        db.session.commit()



