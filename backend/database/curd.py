#对数据库的增删查改操作
from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models

###############USER##################
def get_User_by_Name(db:Session,userName:str):
    return db.query(models.User).filter(models.User.userName==userName).first()

def create_user(db:Session,UserName:str,UserKey:str):
    db_user=models.User(userName=UserName,userKey=UserKey)
    db.add(db_user)
    db.commit()#提交保存到数据库中
    db.refresh(db_user)#刷新
    return db_user

###############Video##################
def get_Video_information(db:Session):
    return db.query(models.Video).all()

def add_Video(db:Session,videoName:str,videoUrl:str,videoDescript:str):
    db_video=models.Video(videoName=videoName,videoUrl=videoUrl,videoDescript=videoDescript)
    db.add(db_video)
    db.commit()#提交保存到数据库中
    db.refresh(db_video)#刷新
    return db_video

def delete_Video(db:Session,videoId:int):
    db_video=db.query(models.Video).filter(models.Video.videoId==videoId).first()
    if db_video:
        db.delete(db_video)
        db.commit()
        # db.refresh()
        # db.close()
        return 1
    else:
        return 0
        
