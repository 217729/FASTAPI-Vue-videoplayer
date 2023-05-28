#表的定义
from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

class User(Base):#普通用户
    __tablename__ = "user"
    # userId=Column(Integer,primary_key=True,autoincrement = True)
    userName = Column(String,primary_key=True,)
    userKey= Column(String)
    
class Video(Base):#视频
    __tablename__="video"
    
    videoId=Column(Integer,primary_key=True)
    videoName=Column(String)
    videoUrl=Column(String)
    videoDescript=Column(String)
    
    