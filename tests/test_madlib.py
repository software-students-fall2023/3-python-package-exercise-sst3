import pytest
import tempfile
from src.sstgame import madlib

def test_readTextEmptyFile():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
        tmp_file.write('')
    prompts = madlib.readText(tmp_file.name)
    assert len(prompts) == 0

def test_readTextFirstLine():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
        tmp_file.write('hello worlds')
    prompts = madlib.readText(tmp_file.name)
    assert len(prompts) == 1
    assert prompts[0] == "hello worlds"

def test_readTextMultipleLines():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
        tmp_file.write('hello worlds \n pineapple')
    prompts = madlib.readText(tmp_file.name)
    assert len(prompts) == 2
    assert prompts[0] == "hello worlds"
    assert prompts[1] == "pineapple"
