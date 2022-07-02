import pymysql
import random


class Conn():
    def __init__(self, user, pwd, db_name):
        self.conn = pymysql.connect(
            host='localhost',
            user=user,
            password=pwd,
            db=db_name,
            charset='utf8',
            # autocommit=True,#如果插入数据，是否自动提交
        )
        # 游标对象用来给数据库发送sql语句，并执行
        self.cur = self.conn.cursor()

    def qry_all(self):
        num = self.cur.execute('select * from joke')  # 执行sql
        print("数据条数：%s" % num)
        if not num: return None
        self.cur.scroll(0, 'absolute')  # 移动到游标最开始
        records = self.cur.fetchall()   # 返回一个可读懂的数据内容
        return records

    def qry_with_id(self, jid):
        # 可以防止sql注入
        num = self.cur.execute('select * from joke where jid=%s', [jid])
        if not num: return None
        self.cur.scroll(0, 'absolute')  # 移动到游标最开始
        return self.cur.fetchone()

    def qry_with_keyword(self, kw):
        # like后面不加双引号，加了以后得不到结果。
        num = self.cur.execute('select * from joke where txt like %s', ["%%%s%%" % kw])
        if not num: return None
        self.cur.scroll(0, 'absolute')  # 移动到游标最开始
        return self.cur.fetchall()

    def random_setence(self):
        num = self.cur.execute('select * from joke')
        if not num: return None
        self.cur.scroll(0, 'absolute')  # 移动到游标最开始
        records = self.cur.fetchall()
        obj = random.choice(records)
        sentence = obj[1]
        return sentence

    def __del__(self):
        self.cur.close()
        self.conn.close()

