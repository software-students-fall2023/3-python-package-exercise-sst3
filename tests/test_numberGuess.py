import pytest
from src.sstgame import numberGuess

def test_chooseRandomPositive():
    result = numberGuess.chooseRandom(1, 3)
    assert result >= 1 and result <= 3

def test_chooseRandomNegative():
    result = numberGuess.chooseRandom(-3, -1)
    assert result >= -3 and result <= -1

def test_chooseRandomPositiveAndNeg():
    result = numberGuess.chooseRandom(-3, 3)
    assert result <= 3 and result >= -3

def test_compareGreaterThan():
    result = numberGuess.compare(0, 100)
    assert result == 1

def test_compareLessThan():
    result = numberGuess.compare(100, 0)
    assert result == -1

def test_compareEqualTo():
    result = numberGuess.compare(0, 0)
    assert result == 0
