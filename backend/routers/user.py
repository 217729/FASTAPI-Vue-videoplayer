from fastapi import APIRouter, Depends, HTTPException, status
from database import curd, models
from dependencies import get_db
from sqlalchemy.orm import Session
from pydantic import BaseModel

router = APIRouter()

#注册
class registerInfo(BaseModel):
    userName:str
    password:str
    
@router.post('/register')
async def register(r:registerInfo,db: Session = Depends(get_db)):
    code=0
    db_user=curd.get_User_by_Name(db=db,userName=r.userName)
    if db_user:
        msg="注册失败，用户名已经存在"
        code=1
        return{
            "code":code,
            "msg":msg,
            "data":db_user.userName
        }
    
    msg="注册成功"
    db_user=curd.create_user(db=db,UserName=r.userName,UserKey=r.password)
    data={}
    data['userName']=db_user.userName
    data['userKey']=db_user.userKey
    return{
        "code":code,
        "msg":msg,
        "data":data
    }
    
@router.post('/login')
async def login(r:registerInfo,db:Session=Depends(get_db)):
    code=0
    db_user=curd.get_User_by_Name(db=db,userName=r.userName)
    if not db_user:
        msg="登录失败！用户名不存在"
        code=1
    elif db_user.userKey==r.password:
        msg="登录成功"
    else:
        msg="密码错误！"
        code=2
    return{
            "code":code,
            "msg":msg
        }
        