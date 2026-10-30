"""Personas: estudiantes y profesores (esquema base §3.1)."""

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    student_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    school: Mapped[str | None] = mapped_column(String(100))
    institution: Mapped[str | None] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    phone: Mapped[str | None] = mapped_column(String(20))
    completed_curriculum: Mapped[bool | None] = mapped_column(Boolean)
    cleared_library: Mapped[bool | None] = mapped_column(Boolean)
    cleared_laboratory: Mapped[bool | None] = mapped_column(Boolean)

    thesis: Mapped["Thesis | None"] = relationship(back_populates="student")  # noqa: F821


class Professor(Base):
    __tablename__ = "professors"

    professor_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    school: Mapped[str | None] = mapped_column(String(100))
    institution: Mapped[str | None] = mapped_column(String(100))
    email: Mapped[str | None] = mapped_column(String(100))  # I-7: sin UNIQUE (se corrige en v2)
