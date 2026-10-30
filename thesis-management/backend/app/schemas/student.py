from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentCreate(BaseModel):
    first_name: str = Field(min_length=1, max_length=100, examples=["Ana"])
    last_name: str = Field(min_length=1, max_length=100, examples=["Torres"])
    email: EmailStr = Field(examples=["ana.torres@uni.edu.ec"])
    school: str | None = Field(
        None, max_length=100, examples=["Mathematical and Computational Sciences"]
    )
    institution: str | None = Field(None, max_length=100)
    phone: str | None = Field(None, max_length=20)
    completed_curriculum: bool = False
    cleared_library: bool = False
    cleared_laboratory: bool = False


class StudentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    student_id: int
    first_name: str
    last_name: str
    email: str
    school: str | None
    institution: str | None
    phone: str | None
    completed_curriculum: bool | None
    cleared_library: bool | None
    cleared_laboratory: bool | None


class Message(BaseModel):
    detail: str
