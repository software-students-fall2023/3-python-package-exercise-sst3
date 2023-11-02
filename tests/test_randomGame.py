from io import StringIO

import pytest
from src.sstgame import randomGame
def test_randomGameRuns(monkeypatch):
    input_string = StringIO("0")
    monkeypatch.setattr('sys.stdin', input_string)

    value = randomGame.randomGame(0, 0, 'test.txt', 'test.txt')

    assert value >= 0

def test_randomGameExcludeAll():
    value = randomGame.randomGame(0, 0, 'test.txt', 'test.txt', madLibAssert=False, numberGuessAssert=False, wyrAssert=False)

    assert value == -1

def test_randomGameExcludeNumberGuess(monkeypatch):
    input_string = StringIO("0")
    monkeypatch.setattr('sys.stdin', input_string)

    value = randomGame.randomGame(0, 0, 'test.txt', 'test.txt', numberGuessAssert=False)

    assert value > 0

def test_randomGameExcludeMadLib(monkeypatch):
    input_string = StringIO("0")
    monkeypatch.setattr('sys.stdin', input_string)

    value = randomGame.randomGame(0, 0, 'test.txt', 'test.txt', madLibAssert=False)

    assert value == 0 or value == 2

def test_randomGameExcludeWyr(monkeypatch):
    input_string = StringIO("0")
    monkeypatch.setattr('sys.stdin', input_string)

    value = randomGame.randomGame(0, 0, 'test.txt', 'test.txt', wyrAssert=False)

    assert value == 0 or value == 1

def test_randomGameOnlyMadLib(monkeypatch):
    input_string = StringIO("0")
    monkeypatch.setattr('sys.stdin', input_string)

    value = randomGame.randomGame(0, 0, 'test.txt', 'test.txt', numberGuessAssert=False, wyrAssert=False)

    assert value == 1

def test_randomGameOnlyNumberGuess(monkeypatch):
    input_string = StringIO("0")
    monkeypatch.setattr('sys.stdin', input_string)

    value = randomGame.randomGame(0, 0, 'test.txt', 'test.txt', madLibAssert=False, wyrAssert=False)

    assert value == 0

def test_randomGameOnlyWyr(monkeypatch):
    input_string = StringIO("0")
    monkeypatch.setattr('sys.stdin', input_string)

    value = randomGame.randomGame(0, 0, 'test.txt', 'test.txt', numberGuessAssert=False, madLibAssert=False)

    assert value == 2