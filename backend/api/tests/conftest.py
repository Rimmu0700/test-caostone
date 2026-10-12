import os

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from sqlalchemy.exc import OperationalError

from src.core.config import get_settings


@pytest.fixture(scope="session")
def db_engine() -> Engine:
    engine = create_engine(get_settings().database_url)
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
    except OperationalError:
        if os.environ.get("CI") == "true":
            raise
        pytest.skip("PostgreSQL tidak dapat dijangkau, tes basis data dilewati")
    yield engine
    engine.dispose()
