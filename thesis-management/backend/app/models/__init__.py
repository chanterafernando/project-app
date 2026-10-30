"""Importa todos los modelos para que queden registrados en Base.metadata."""

from app.models.people import Professor, Student
from app.models.thesis import (
    AcademicPeriod,
    Defense,
    PlagiarismCheck,
    Requirement,
    ReviewerAssignment,
    Thesis,
    ThesisPeriod,
    TutorAssignment,
)

__all__ = [
    "AcademicPeriod",
    "Defense",
    "PlagiarismCheck",
    "Professor",
    "Requirement",
    "ReviewerAssignment",
    "Student",
    "Thesis",
    "ThesisPeriod",
    "TutorAssignment",
]
