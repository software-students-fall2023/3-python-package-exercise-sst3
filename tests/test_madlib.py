import pytest
import tempfile
from src.sstgame import madlib

def test_readTextEmptyFile():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
        tmp_file.write('')
    prompts = madlib.readText(tmp_file.name)
    assert len(prompts) == 0

def test_extractWordsEmpty():
    matches = madlib.extractWords("This is something that has no extraction")
    assert len(matches) == 0

def test_extractWordsOne():
    matches = madlib.extractWords("There should be one extraction here [verb]")
    assert len(matches) == 1
    assert matches[0] == "verb"

def test_extractWordsMultiple():
    matches = madlib.extractWords("There should be [multiple] [extractions] here [verb]")
    assert len(matches) == 3
    assert matches[0] == "multiple"
    assert matches[1] == "extractions"
    assert matches[2] == "verb"

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
