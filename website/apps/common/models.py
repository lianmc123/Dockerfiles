from exts import db
from datetime import datetime
from sqlalchemy.dialects.mysql import LONGTEXT


class BannerModel(db.Model):
    __tablename__ = "banner"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    link_url = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.INTEGER, default=0)
    is_show = db.Column(db.INTEGER, default=0)
    create_time = db.Column(db.DATETIME, default=datetime.now)


class BoardModel(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    is_show = db.Column(db.INTEGER, default=0)
    create_time = db.Column(db.DATETIME, default=datetime.now)


class PostModel(db.Model):
    __tablename__ = "post"
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    is_show = db.Column(db.INTEGER, default=1)
    create_time = db.Column(db.DATETIME, default=datetime.now)
    board_id = db.Column(db.INTEGER, db.ForeignKey("board.id"), nullable=False)
    author_id = db.Column(db.String(100), db.ForeignKey("front_user.uid"), nullable=False)

    board = db.relationship("BoardModel", backref="posts")
    author = db.relationship("FrontUser", backref="posts")

    __mapper_args__ = {
        "order_by": create_time.desc()  # 使用标题排序
    }


class HighlightPostModel(db.Model):
    __tablename__ = 'highlight_post'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    post_id = db.Column(db.INTEGER, db.ForeignKey('post.id'), nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)
    post = db.relationship("PostModel", backref='highlight')


class CommentModel(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DATETIME, default=datetime.now)
    post_id = db.Column(db.INTEGER, db.ForeignKey('post.id'), nullable=False)
    is_show = db.Column(db.INTEGER, default=1)
    author_id = db.Column(db.String(100), db.ForeignKey('front_user.uid'), nullable=False)

    post = db.relationship("PostModel", backref='comments')
    author = db.relationship("FrontUser", backref='comments')


class News(db.Model):
    __tablename__ = 'news'
    a_id = db.Column(db.String(32), primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    cover_img = db.Column(db.Text)
    content = db.Column(LONGTEXT, nullable=False)
    channel = db.Column(db.String(10), nullable=False)
    pubtime = db.Column(db.DATETIME, default=datetime(2018, 1, 1, 0, 0, 0))
    url = db.Column(db.String(255))
    crawl_time = db.Column(db.DATETIME, default=datetime.now)
    update_time = db.Column(db.DATETIME, default=datetime.now)

    __mapper_args__ = {
        "order_by": pubtime.desc()
    }
