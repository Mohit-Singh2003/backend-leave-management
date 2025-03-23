from fastapi import APIRouter, Depends, HTTPException, status
from services.leave_service import (
    create_leave_request,
    get_all_leaves,
    update_leave_status,
)
from models import LeaveRequest, LeaveResponse
from utils import get_current_user

router = APIRouter(
    prefix="/leaves",
    tags=["Leaves"]
)

# POST /leaves/submit -> Submit a leave request (Employee)
@router.post("/submit", status_code=status.HTTP_201_CREATED)
async def submit_leave(leave: LeaveRequest, user=Depends(get_current_user)):
    if user['role'] != 'employee':
        raise HTTPException(status_code=403, detail="Only employees can submit leaves.")
    
    await create_leave_request(leave, user)
    return {"message": "Leave request submitted successfully."}


# GET /leaves/ -> Manager or Employee can view leave requests
@router.get("/", response_model=list[LeaveResponse])
async def list_leaves(user=Depends(get_current_user)):
    leaves = await get_all_leaves(user)
    return leaves


# PUT /leaves/{leave_id}/{status} -> Manager updates status
@router.put("/{leave_id}/{status}", status_code=status.HTTP_200_OK)
async def change_leave_status(
    leave_id: str,
    status: str,
    user=Depends(get_current_user)
):
    if user['role'] != 'manager':
        raise HTTPException(status_code=403, detail="Only managers can update leave status.")
    
    if status.lower() not in ['approved', 'rejected']:
        raise HTTPException(status_code=400, detail="Invalid status. Use 'approved' or 'rejected'.")
    
    await update_leave_status(leave_id, status)
    return {"message": f"Leave {status} successfully."}
