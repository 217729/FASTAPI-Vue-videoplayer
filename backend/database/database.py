from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+pymysql://root:your_password@127.0.0.1:3306/video_player"
    #”drivername://root:password@127.0.0.0:3306(port)/database_name"
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()