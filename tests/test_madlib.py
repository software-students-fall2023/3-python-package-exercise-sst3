import pytest
from src.sstgame import madlib

def test_first():
    assert 3 == 3

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