import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

@dataclass
class Project:
    id: int
    name: str
    compliance_status: str
    recent_violations: List[str]

@dataclass
class Dashboard:
    total_projects: int
    compliance_status: str
    recent_violations: List[str]

def get_projects():
    # Simulate fetching projects from a database
    projects = [
        Project(1, "Project 1", "Compliant", ["Violation 1"]),
        Project(2, "Project 2", "Non-Compliant", ["Violation 2", "Violation 3"]),
        Project(3, "Project 3", "Compliant", []),
    ]
    return projects

def get_dashboard(projects):
    total_projects = len(projects)
    compliance_status = "Compliant" if all(project.compliance_status == "Compliant" for project in projects) else "Non-Compliant"
    recent_violations = [violation for project in projects for violation in project.recent_violations]
    return Dashboard(total_projects, compliance_status, recent_violations)

def get_project_logs(project_id, projects):
    for project in projects:
        if project.id == project_id:
            return project
    return None

def refresh_metrics(dashboard, projects):
    # Simulate refreshing metrics every 5 minutes
    dashboard.total_projects = len(projects)
    dashboard.compliance_status = "Compliant" if all(project.compliance_status == "Compliant" for project in projects) else "Non-Compliant"
    dashboard.recent_violations = [violation for project in projects for violation in project.recent_violations]
    return dashboard

def drill_down_into_project_logs(project_id, projects):
    project = get_project_logs(project_id, projects)
    if project:
        return project
    else:
        raise ValueError("Project not found")
