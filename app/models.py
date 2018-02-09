from app.exts import db


class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    puid = db.Column(db.String)
    nick_name = db.Column(db.String)
    remark_name = db.Column(db.String)
    sex_id = db.Column(db.Integer, db.ForeignKey('sex.id'))
    signature = db.Column(db.String)
    province = db.Column(db.String)
    city = db.Column(db.String)
    call = db.Column(db.String)

    def __repr__(self):
        return f'<Firend {self.nick_name}>'


class Sex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String)
    friends = db.relationship('Friend', backref=db.backref('sex', lazy=True))

    def __repr__(self):
        return f'<Sex {self.label}>'
