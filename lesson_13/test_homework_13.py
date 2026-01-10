import pytest
from pathlib import Path
from homework_13 import log_event


log_event(username="admin", status="success")
log_event(username="user", status="expired")
log_event(username="unknown", status="failed")

LOG_FILE = Path(__file__).parent / "login_system.log"
def test_logger_success():
       with open("login_system.log", "r") as f:
        content = f.read()
        assert "INFO" in content
        assert "Username: admin, Status: success" in content


def test_logger_warning():
    with open("login_system.log", "r") as f:
        content = f.read()
        assert "WARNING" in content
        assert "Username: user, Status: expired" in content

def test_logger_error():
    with open("login_system.log", "r") as f:
        content = f.read()
        assert "ERROR" in content
        assert "Username: unknown, Status: failed" in content