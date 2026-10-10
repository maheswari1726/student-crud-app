from sqlalchemy import Column,Integer,String,Date
from database import Base
class Student(Base):
    __tablename__="STUDENTS"
    id=Column(Integer,primary_key=True,index=True)
    student_id=Column(String,unique=True,index=True,nullable=False)
    student_name=Column(String,nullable=False)
    date_of_birth=Column(Date,nullable=False)
    email=Column(String,unique=True,nullable=False)
    phone=Column(String,nullable=True)
