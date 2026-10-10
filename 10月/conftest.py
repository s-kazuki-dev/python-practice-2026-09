
import pytest

@pytest.fixture
def sample_records():
    return  [
        {"date": "2026-10-06", "subject": "Python", "minutes": 90},
        {"date": "2026-10-07", "subject": "Python", "minutes": 120},
        {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
    ]
