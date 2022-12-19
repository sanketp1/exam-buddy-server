from database import Base
from sqlalchemy import Column, Integer,String, Boolean

# class MediaContent(Base):
#     __tablename__ = "mediacontent"
#     id = Column(Integer,primary_key = True, index=True, nullable= False)
#     title = Column(String, nullable = False)
#     desc = Column(String, nullable = True)
#     category = Column(String, nullable = True)
#     mediaLink = Column(String,nullable = True)
#     banner = Column(String,nullable = True)

class Users(Base):
    __tablename__ = "users"
    avatar = Column(String,nullable = True)
    uid = Column(String, primary_key = True, nullable = False)
    name = Column(String, nullable = False)
    email = Column(String, nullable = False)
    password = Column(String, nullable = False)
    field_of_study =Column(String, nullable = True)
    branch = Column(String,nullable = True)
    year_of_study = Column(String, nullable=True) 