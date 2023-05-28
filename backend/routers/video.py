from fastapi import APIRouter, Depends, HTTPException, status
from database import curd, models
from dependencies import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel

router = APIRouter()

#视频信息
class videoInfo(BaseModel):
    videoName:str
    videoUrl:str
    videoDescript:str
    
@router.post('/add_vedio')
async def add_vedio(r:videoInfo,db: Session = Depends(get_db)):
    code=0
    db_video=curd.add_Video(db=db,videoName=r.videoName,videoUrl=r.videoUrl,videoDescript=r.videoDescript)
    msg="视频添加成功"
    data={}
    data['videoId']=db_video.videoId
    data['videoName']=db_video.videoName
    return{
        "code":code,
        "msg":msg,
        "data":data
    }
    
@router.get('/all_vedio')
async def get_all(db:Session=Depends(get_db)):
    code=0
    db_vedio=curd.get_Video_information(db=db)
    msg="视频查询完毕"
    data=[]
    return{
        "code":code,
        "msg":msg,
        "data":db_vedio
    }
    
@router.get('/delete_vedio/{vedioId}')
async def delete_id(vedioId:int,db:Session=Depends(get_db)):
    # code=0
    res=curd.delete_Video(db=db,videoId=vedioId)
    if res:
        return {"code": "0000", "message": "删除成功"}
    else:
        return {"code": "0001", "message": "不存在对象"}

