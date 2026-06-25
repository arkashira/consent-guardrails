import pytest
from consent_guardrails import get_projects, get_dashboard, get_project_logs, refresh_metrics, drill_down_into_project_logs

def test_get_projects():
    projects = get_projects()
    assert len(projects) == 3

def test_get_dashboard():
    projects = get_projects()
    dashboard = get_dashboard(projects)
    assert dashboard.total_projects == 3
    assert dashboard.compliance_status == "Non-Compliant"
    assert len(dashboard.recent_violations) == 3

def test_get_project_logs():
    projects = get_projects()
    project = get_project_logs(1, projects)
    assert project.name == "Project 1"

def test_refresh_metrics():
    projects = get_projects()
    dashboard = get_dashboard(projects)
    refreshed_dashboard = refresh_metrics(dashboard, projects)
    assert refreshed_dashboard.total_projects == 3
    assert refreshed_dashboard.compliance_status == "Non-Compliant"
    assert len(refreshed_dashboard.recent_violations) == 3

def test_drill_down_into_project_logs():
    projects = get_projects()
    project = drill_down_into_project_logs(1, projects)
    assert project.name == "Project 1"

def test_drill_down_into_project_logs_project_not_found():
    projects = get_projects()
    with pytest.raises(ValueError):
        drill_down_into_project_logs(4, projects)
