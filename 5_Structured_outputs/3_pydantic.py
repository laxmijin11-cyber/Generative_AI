#  pip install pydantic
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):

    name: str = "Anshu"
    age: Optional[int] = None
    # imp to set optional value as Noneor something default
    email: EmailStr
    cgpa: float = Field(
        gt=0,
        lt=10,
        default=5,
        description="a decimal value representing cgpa  of the student",
    )


new_student = {"name": "aarohi", "age": "32", "email": "abc@gmail.com", "cgpa": 12}
# new_student = {"name": 25}

student1 = Student(**new_student)
print(type(student1))
print(student1)
print(student1.name)
student_dict = dict(student1)
print(student_dict["age"])

student_json = student1.model_dump_json()
# pydantic is smart enough to convert some daata types like its coerce
# pip install 'pydantic[email]
