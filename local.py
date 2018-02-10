from app import create_app
from app.models import Friend
from app.exts import db

from wxpy import Bot
from time import sleep
from random import randint
from retrying import retry

app = create_app()
app.app_context().push()

f = Friend()


def login():
    bot = Bot(True)
    bot.enable_puid()
    return bot


def set_remark(friend):
    @retry(wait_fixed=randint(60, 120) * 1e4)
    def do():
        print('[*] SET REMARK', remark_name)
        friend.set_remark_name(remark_name)
        sleep(randint(3, 6))

    nick_name = friend.nick_name
    record = f.query.filter_by(nick_name=nick_name).first()

    if record:
        remark_name = record.remark_name
        if friend.remark_name == remark_name:
            print('[*] PASS')
        else:
            do()

    else:
        # 好友不在数据库中，保存至数据库
        print('[*] ADD')
        for field in ['puid', 'nick_name', 'remark_name', 'signature', 'province', 'city']:
            setattr(f, field, getattr(friend, field))
        f.sex_id = friend.sex
        db.session.add(f)
        db.session.commit()


def send_message(friend):
    pass


if __name__ == '__main__':
    bot = login()
    friends = bot.friends()

    for i, each in enumerate(friends[2:]):
        print(f'[{i}] {each.nick_name}')
        set_remark(each)

        # if (i > 0) and (i % 10 == 0):
        #     sleep(randint(10,20))
