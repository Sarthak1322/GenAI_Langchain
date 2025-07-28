from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name:str = 'Sar' #default value set  
    age: Optional[int] = None
    email: EmailStr
    cgpa:float = Field(gt=0, lt=10, default=5)  #greater than less than


new_student = {'name':'Sarthak',
               'email': 'sarthak@gmail.com'} 

student = Student(**new_student)

student_dict = dict(student)
student_json = student.model_dump_json(student)

print(student)


 
