"""Tesis y su seguimiento (esquema base §3.1 del documento de punto de partida).

Este es el esquema heredado de thesis_api/models.py reescrito en SQLAlchemy 2.0
(DEC-11). Las correcciones de la v2 (§8) se aplicarán como migraciones nuevas.
"""

import datetime as dt
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    Date,
    Enum,
    ForeignKey,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class AcademicPeriod(Base):
    __tablename__ = "academic_periods"

    period_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    start_date: Mapped[dt.date | None] = mapped_column(Date)
    end_date: Mapped[dt.date | None] = mapped_column(Date)


class Thesis(Base):
    __tablename__ = "theses"

    thesis_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255))
    abstract: Mapped[str | None] = mapped_column(Text)
    status: Mapped[str | None] = mapped_column(String(50), default="Draft")
    stage: Mapped[str | None] = mapped_column(String(50), default="Thesis I")
    student_id: Mapped[int] = mapped_column(ForeignKey("students.student_id"), unique=True)

    student: Mapped["Student"] = relationship(back_populates="thesis")  # noqa: F821


class ThesisPeriod(Base):
    __tablename__ = "thesis_period"

    thesis_id: Mapped[int] = mapped_column(ForeignKey("theses.thesis_id"), primary_key=True)
    period_id: Mapped[int] = mapped_column(
        ForeignKey("academic_periods.period_id"), primary_key=True
    )


class TutorAssignment(Base):
    __tablename__ = "tutor_assignments"

    thesis_id: Mapped[int] = mapped_column(ForeignKey("theses.thesis_id"), primary_key=True)
    professor_id: Mapped[int] = mapped_column(
        ForeignKey("professors.professor_id"), primary_key=True
    )
    # I-1: la PK incluye role; DEC-03 la cambiará a (thesis_id, role) en la v2.
    role: Mapped[str] = mapped_column(
        Enum("Tutor", "Co-Tutor", name="tutor_role"), primary_key=True
    )


class ReviewerAssignment(Base):
    __tablename__ = "reviewer_assignments"

    thesis_id: Mapped[int] = mapped_column(ForeignKey("theses.thesis_id"), primary_key=True)
    professor_id: Mapped[int] = mapped_column(
        ForeignKey("professors.professor_id"), primary_key=True
    )
    role: Mapped[str | None] = mapped_column(String(50))  # 'Committee' | 'President'
    comments: Mapped[str | None] = mapped_column(Text)
    revision_corrected: Mapped[bool | None] = mapped_column(Boolean)


class Requirement(Base):
    __tablename__ = "requirements"

    requirement_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    thesis_id: Mapped[int] = mapped_column(ForeignKey("theses.thesis_id"))
    name: Mapped[str] = mapped_column(String(100))
    status: Mapped[bool | None] = mapped_column(Boolean)


class PlagiarismCheck(Base):
    __tablename__ = "plagiarism_checks"

    check_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    thesis_id: Mapped[int] = mapped_column(ForeignKey("theses.thesis_id"), unique=True)
    similarity_percentage: Mapped[Decimal | None] = mapped_column(Numeric(5, 2))


class Defense(Base):
    __tablename__ = "defenses"

    defense_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    thesis_id: Mapped[int] = mapped_column(ForeignKey("theses.thesis_id"), unique=True)
    # Atributos con nombre de columna explícito para no chocar con los tipos date/time.
    defense_date: Mapped[dt.date | None] = mapped_column("date", Date)
    defense_time: Mapped[str | None] = mapped_column("time", String(50))  # I-6 (DEC-09 en v2)
    location: Mapped[str | None] = mapped_column(String(100))
    modality: Mapped[str | None] = mapped_column(String(50))  # 'In-person' | 'Virtual'
    final_grade: Mapped[Decimal | None] = mapped_column(Numeric(4, 2))
