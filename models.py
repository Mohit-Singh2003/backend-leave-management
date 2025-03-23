from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    id: str
    username: str
    role: str

class LeaveRequest(BaseModel):
    employee_id: str
    leave_type: str
    start_date: date
    end_date: date
    reason: str

class LeaveResponse(LeaveRequest):
    id: str
    status: str
    is_active: bool
