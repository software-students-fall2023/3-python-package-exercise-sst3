import pytest
import tempfile
from src.sstgame import wyr
from io import StringIO

def test_wouldYouRather(capfd, monkeypatch):
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
        tmp_file.write('Would you rather eat food or drink water')

    inputString = StringIO("drink water")
    monkeypatch.setattr('sys.stdin', inputString)

    wyr.wouldYouRather(tmp_file.name)

    captured = capfd.readouterr()

    assert "Would you rather eat food or drink water\nPlease enter Yes or No"==captured.out 
