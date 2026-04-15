

from pydantic import BaseModel

class student_detail_validation(BaseModel):
    id : int
    name : str
    roll : int
    city : str = None