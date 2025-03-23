from models import LeaveRequest
from utils import get_bigquery_client
import uuid

async def create_leave_request(leave: LeaveRequest, user: dict):
    client = get_bigquery_client()
    leave_id = str(uuid.uuid4())

    row = {
        "id": leave_id,
        "employee_email": user["email"],
        "start_date": leave.start_date,
        "end_date": leave.end_date,
        "reason": leave.reason,
        "status": "Pending",
        "is_active": True
    }

    errors = client.insert_rows_json("your-dataset.leaves", [row])
    if errors:
        raise Exception(f"Failed to insert leave request: {errors}")
    return row

async def get_all_leaves(user: dict):
    client = get_bigquery_client()
    query = "SELECT * FROM `your-dataset.leaves` WHERE is_active = TRUE"

    if user["role"] == "employee":
        query += f" AND employee_email = '{user['email']}'"

    query_job = client.query(query)
    results = [dict(row) for row in query_job]
    return results

async def update_leave_status(leave_id: str, status: str):
    client = get_bigquery_client()
    query = f"""
    UPDATE `your-dataset.leaves`
    SET status = '{status.capitalize()}'
    WHERE id = '{leave_id}' AND is_active = TRUE
    """
    query_job = client.query(query)
    query_job.result()  # wait for completion
