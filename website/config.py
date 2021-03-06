import os
from datetime import timedelta

# ------------ app.run()相关参数---------------
DEBUG = False
# ----------------- 分割线 --------------------

# ------------- SQLAlchemy 相关----------------
DB_HOST = 'mysql'
DB_PORT = 3306
DATABASE = 'website'
DB_USERNAME = 'root'
DB_PASSWORD = 'lianmc123456'
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}" \
         "?charset=utf8".format(username=DB_USERNAME,
                                password=DB_PASSWORD, host=DB_HOST,
                                port=DB_PORT, db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
# ----------------- 分割线 ---------------------

# -------------- session相关 -------------------
# SECRET_KEY = os.urandom(24)
SECRET_KEY = "a6sd51as5d1asd66"
PERMANENT_SESSION_LIFETIME = timedelta(days=7)
# ----------------- 分割线 ---------------------

# ----------------- 常量 -----------------------
CMS_USER_ID = "ASDGFSDF"
FRONT_USER_ID = 'oqerhfoasf'
# ----------------- 分割线 ---------------------

# ----------------- 邮箱 -----------------------
MAIL_SERVER = "smtp.126.com"
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = "q135025@126.com"
MAIL_PASSWORD = "bnmbnm123123"
MAIL_DEFAULT_SENDER = "q135025@126.com"
MAIL_DEBUG = False
# ----------------- 分割线 ---------------------

# ----------------- 阿里大于 -----------------------
ALIDAYU_APP_KEY = 'LTAIfbaYxJm4sWQZ'
ALIDAYU_APP_SECRET = 'K8q1CPvkFNYeRuMqIMtlQUfBDWBJNv'
ALIDAYU_SIGN_NAME = '易秀米'
ALIDAYU_TEMPLATE_CODE = 'SMS_126635198'
# ----------------- 分割线 ---------------------

# ----------------- 短信验证码 -----------------
SMS_SALT = "sodhfoaw201rkqwuhro"
# ----------------- 分割线 ---------------------

# ----------------- UEditor -----------------
UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')
UEDITOR_UPLOAD_TO_QINIU = False
UEDITOR_QINIU_ACCESS_KEY = "M4zCEW4f9XPanbMN-Lb9O0S8j893f0e1ezAohFVL"
UEDITOR_QINIU_SECRET_KEY = "7BKV7HeEKM3NDJk8_l_C89JI3SMmeUlAIatzl9d4"
UEDITOR_QINIU_BUCKET_NAME = "hyvideo"
UEDITOR_QINIU_DOMAIN = 'http://7xqenu.com1.z0.glb.clouddn.com'
# ----------------- 分割线 ---------------------

# -------------- flask-paginate ---------------
PER_PAGE = 10
# ----------------- 分割线 ---------------------
# -------------- Celery ---------------
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
# ----------------- 分割线 ---------------------
