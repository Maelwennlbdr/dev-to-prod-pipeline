import pytest
from datetime import date, timedelta
from models import Task, User
from app import _build_postgres_uri
import os

def test_task_overdue_true():
    task = Task(title="Overdue Task", due_date=date.today() - timedelta(days=1))
    assert task.is_overdue() is True

def test_task_overdue_false():
    task = Task(title="Future Task", due_date=date.today() + timedelta(days=1))
    assert task.is_overdue() is False

def test_user_password_hashing():
    user = User(username="testuser")
    user.set_password("secret")
    assert user.check_password("secret") is True
    assert user.check_password("wrong") is False

def test_build_postgres_uri():
    user = os.environ.get("POSTGRES_USER", "postgres")
    password = os.environ.get("POSTGRES_PASSWORD", "postgres")
    host = os.environ.get("POSTGRES_HOST", "localhost")
    port = os.environ.get("POSTGRES_PORT", "5432")
    name = os.environ.get("POSTGRES_DB", "taskmanager")

    uri = _build_postgres_uri()
    assert uri.startswith(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}")

