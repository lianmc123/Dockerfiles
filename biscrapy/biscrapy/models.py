from sqlalchemy import create_engine, Column, DATETIME, Text, String, ForeignKey, INTEGER, MetaData, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from biscrapy.settings import DB_URI
from sqlalchemy.dialects.mysql import LONGTEXT
from datetime import datetime

engine = create_engine(DB_URI)
Base = declarative_base(engine)
metadata = MetaData()


# class NewsExtend(Base):
#     __tablename__ = 'news_extend'
#     id = Column(INTEGER, primary_key=True, autoincrement=True)
#     cover_img = Column(Text)
#     content = Column(LONGTEXT, nullable=False)
#     channel = Column(String(10), nullable=False)
#     pubtime = Column(String(32))
#     url = Column(String(255))
#     crawl_time = Column(DATETIME, default=datetime.now)
#     update_time = Column(DATETIME, default=datetime.now)
#     a_id = Column(String(32), ForeignKey('news.a_id'), nullable=False)
#     news = relationship('News', backref=backref('extend', uselist=False))


class News(Base):
    __tablename__ = 'news'
    a_id = Column(String(32), primary_key=True)
    title = Column(String(50), nullable=False)
    cover_img = Column(Text)
    content = Column(LONGTEXT, nullable=False)
    channel = Column(String(10), nullable=False)
    pubtime = Column(DATETIME, default=datetime(2018, 1, 1, 0, 0, 0))
    url = Column(String(255))
    crawl_time = Column(DATETIME, default=datetime.now)
    update_time = Column(DATETIME, default=datetime.now)


# news = Table('news', metadata,
#              Column('a_id', String(32), primary_key=True),
#              Column('title', String(50), nullable=False)
#              )
#
# news_extend = Table('news_extend', metadata,
#                     Column('id', INTEGER, primary_key=True, autoincrement=True),
#                     Column('cover_img', Text),
#                     Column('content', LONGTEXT, nullable=False),
#                     Column('channel', String(10), nullable=False),
#                     Column('pubtime', String(32)),
#                     Column('url', String(255)),
#                     Column('crawl_time', DATETIME, default=datetime.now),
#                     Column('update_time', DATETIME, default=datetime.now),
#                     Column('a_id', String(32), ForeignKey('news.a_id'), nullable=False),
#                     )

Base.metadata.create_all()

# Base.metadata.drop_all()
# Base.metadata.create_all()
