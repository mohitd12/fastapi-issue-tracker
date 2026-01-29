import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueOutput, IssueUpdate, IssueStatus, IssuePriority
from app.storage import load_data, save_data

router = APIRouter(prefix="/api/issues", tags=["issues"])

@router.get("/", response_model=list[IssueOutput])
async def get_issues():
  issues = load_data()
  return issues

@router.post("/", response_model=IssueOutput, status_code=status.HTTP_201_CREATED)
async def create_issue(payload: IssueCreate):
  issues = load_data()
  new_issue = {
    "id": str(uuid.uuid4()),
    "title": payload.title,
    "description": payload.description,
    "status": IssueStatus.open,
    "priority": IssuePriority.medium,
  }
  issues.append(new_issue)
  save_data(issues)
  return new_issue

@router.get("/{issue_id}", response_model=IssueOutput)
def get_issue(issue_id: str):
  issues = load_data()
  for issue in issues:
    if issue["id"] == issue_id:
      return issue
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.put("/{issue_id}", response_model=IssueOutput)
async def update_issue(issue_id: str, payload: IssueUpdate):
  issues = load_data()
  for index, issue in enumerate(issues):
    if issue["id"] == issue_id:
      updated_issue = issue.copy()
      if payload.title is not None:
        updated_issue["title"] = payload.title
      if payload.description is not None:
        updated_issue["description"] = payload.description
      if payload.status is not None:
        updated_issue["status"] = payload.status
      if payload.priority is not None:
        updated_issue["priority"] = payload.priority
      issues[index] = updated_issue
      save_data(issues)
      return updated_issue
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")

@router.delete("/{issue_id}")
def delete_issue(issue_id: str):
  issues = load_data()
  for index, issue in enumerate(issues):
    if issue["id"] == issue_id:
      issues.pop(index)
      save_data(issues)
      return
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Issue not found")
