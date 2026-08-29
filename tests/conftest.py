from __future__ import annotations

from pathlib import Path

import pytest

pytest_plugins = ("sphinx.testing.fixtures",)


@pytest.fixture(scope="session")
def rootdir() -> Path:
    return Path(__file__).resolve().parent / "roots"
