from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Student
from app.schemas.student import Message, StudentCreate, StudentOut

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("", response_model=list[StudentOut], summary="Listar estudiantes")
def list_students(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    db: Session = Depends(get_db),
):
    stmt = select(Student).order_by(Student.student_id).offset(skip).limit(limit)
    return db.scalars(stmt).all()


@router.get(
    "/{student_id}",
    response_model=StudentOut,
    summary="Obtener un estudiante",
    responses={404: {"model": Message}},
)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.get(Student, student_id)
    if student is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Estudiante no encontrado")
    return student


@router.post(
    "",
    response_model=StudentOut,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar un estudiante",
    responses={409: {"model": Message, "description": "Email ya registrado"}},
)
def create_student(body: StudentCreate, db: Session = Depends(get_db)):
    email = body.email.lower()
    if db.scalar(select(Student.student_id).where(func.lower(Student.email) == email)):
        raise HTTPException(status.HTTP_409_CONFLICT, "El email ya está registrado")
    student = Student(**body.model_dump(exclude={"email"}), email=email)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student
