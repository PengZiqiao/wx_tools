from flask_script import Manager
from app import app
from app.models import *

manager = Manager(app)


@manager.command
def db_init():
    db.drop_all()
    db.create_all()
    for i, label in enumerate(['外星人', '先生', '女士']):
        sex = Sex()
        sex.id, sex.label = i, label
        db.session.add(sex)
    db.session.commit()

@manager.command
def db_drop():
    db.drop_all()

@manager.command
def db_create():
    db.create_all()
    for i, label in enumerate(['外星人', '先生', '女士']):
        sex = Sex()
        sex.id, sex.label = i, label
        db.session.add(sex)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
