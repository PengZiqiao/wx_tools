from flask_restful import Resource
from wxpy import Bot
from flask import url_for
from app.models import Friend
from app.exts import db
from time import sleep

g = dict()


class Login(Resource):
    def get(self):
        if 'bot' not in g:
            g['bot'] = Bot(cache_path=True)
            g['bot'].enable_puid()
        return {'message': 'Complated !'}


class Friends(Resource):
    def get(self):
        if 'bot' in g:
            g['friends'] = g['bot'].friends()
            return {'len': len(g['friends'])}
        else:
            return {'message': 'Login, please!'}


class SaveFriends(Resource):
    def get(self):
        if ('bot' in g) and ('friends' in g):

            # 遍历全部好友
            for i, each in enumerate(g['friends']):
                friend = Friend()
                print(i, each.nick_name)

                # 遍历字段
                for field in ['puid', 'nick_name', 'remark_name', 'signature', 'province', 'city']:
                    setattr(friend, field, getattr(each, field))
                friend.sex_id = each.sex

                # 保存至数据库
                db.session.add(friend)

                # 保存文件
                each.get_avatar(f'e:/avatar/{each.puid}.png')

            db.session.commit()
            return {'message': 'ok!'}
        else:
            Login().get()
            Friends().get()
            return {'message': 'try again.'}


class SetRemark(Resource):
    def get(self):
        if ('bot' in g) and ('friends' in g):
            f = Friend()
            for i, each in enumerate(g['friends'][1:]):
                nick_name = each.nick_name
                friend = f.query.filter_by(nick_name=nick_name).first()
                print(i, nick_name, friend.remark_name)
                if each.remark_name == friend.remark_name:
                    print('PASS')
                    continue
                else:
                    try:
                        each.set_remark_name(friend.remark_name)
                        sleep(3)
                    except:
                        print('FAIL')
            return {'message': 'ok.'}

        else:
            Login().get()
            Friends().get()
            return {'message': 'try again.'}
