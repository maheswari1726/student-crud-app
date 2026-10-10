from datetime import date
from pydantic import BaseModel,EmailStr,ConfigDict
class StudentCreate(BaseModel):
    student_id:str
    student_name:str
    date_of_birth:date
    email:EmailStr
    phone:str | None=None

class StudentResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    student_id:str
    student_name:str
    date_of_birth:date
    email:EmailStr
    phone:str |None=None