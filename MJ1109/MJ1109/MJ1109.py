import sqlite3 as sqlite
from werkzeug import check_password_hash,generate_password_hash

def init_db():
    db = sqlite.connect("test.db")
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
        db.commit()

def get_db():
    db = sqlite.connect("test.db")
    return db
def register():
    db = get_db()
    cur = db.cursor()
    userid = str(input("ID를 입력하세요:"))
    checksql = "select userpw from user where userid = '"+userid+"'"
    cur.execute(checksql)
    length = cur.fetchall()
    if len(length) != 0:
        print("ID가 이미 존재합니다.")
        return
    username = str(input("이름를 입력하세요:"))
    userpw = userid = str(input("비밀번호를 입력하세요:"))
    pw = generate_password_hash(userpw)
    insertsql = "insert into user(userid,username,userpw) values('"+userid+"','"+username+"','"+pw+"')"
    cur.execute(insertsql)
    db.commit()
def login():
    db = get_db()
    cur = db.cursor()
    userid = str(input("ID를 입력하세요:"))
    userpw = str(input("비밀번호를 입력하세요:"))
    loginsql = "select * from user where userid = ?"
    cur.execute(loginsql,[userid])
    user = cur.fetchone()
    if (user == None) :
        print("아디없음")
    elif check_password_hash(user[3], userpw):
        print("로그인성공")
    else:
        print("비번틀림")


init_db()
register()
login()
#register()