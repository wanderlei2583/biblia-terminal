import json
import shutil
from pathlib import Path

import pytest
from bb.books import Book

FIXTURE = Path(__file__).parent / "fixtures" / "mini_bible.json"


@pytest.fixture
def bible() -> list[Book]:
    with FIXTURE.open(encoding="utf-8") as f:
        data: list[Book] = json.load(f)
    return data


@pytest.fixture
def data_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Aponta o bb para uma pasta temporária com a Bíblia de teste."""
    shutil.copy(FIXTURE, tmp_path / "acf.json")
    monkeypatch.setenv("BB_DATA_DIR", str(tmp_path))
    return tmp_path
