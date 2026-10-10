from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from model import Student
from schemas import StudentCreate, StudentResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Database CRUD API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Student Database CRUD API is running"}


@app.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    existing = db.query(Student).filter(
        (Student.student_id == student.student_id) |
        (Student.email == student.email)
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Student ID or email already exists"
        )

    new_student = Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@app.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: str, db: Session = Depends(get_db)):
    student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: str,
    updated_data: StudentCreate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    duplicate = db.query(Student).filter(
        Student.email == updated_data.email,
        Student.student_id != student_id
    ).first()

    if duplicate:
        raise HTTPException(status_code=400, detail="Email already exists")

    for key, value in updated_data.model_dump().items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return student


@app.delete("/students/{student_id}")
def delete_student(student_id: str, db: Session = Depends(get_db)):
    student = db.query(Student).filter(
        Student.student_id == student_id
    ).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}