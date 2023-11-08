import pytest
import os
from src.sstgame.anagram import makeSet, generateLetters, is_valid_answer, calcScore
from io import StringIO

@pytest.fixture
def words_set():
    package_dir = os.path.dirname(__file__)
    fileName = os.path.join(package_dir, "anagram.txt")
    return makeSet(fileName)

def test_len_generateLetters():
    letters = generateLetters(7)

    assert len(letters)==7 #Check if the result of generateLetters is the proper length
    assert any(letter in 'aeiou' for letter in letters) #Check if there is a vowel in letters
     
    

def test_is_valid_answer(words_set):
    letters = ['p','e','a','r']

    assert is_valid_answer(words_set, 'pear', letters) == True #should work
    assert is_valid_answer(words_set, 'apple', letters) == False #should not work
    assert is_valid_answer(words_set, 'pears', letters) == False #should not work
    assert is_valid_answer(words_set, 'ear', letters) == True #should work, only uses some letters
    assert is_valid_answer(words_set, 'r', letters) == False #Should not work, not a work

def test_calcScore():
    letters = ['p','e','a','r']

    assert calcScore('ear', letters) == 30 # 3 * 10 for base score, doesn't use all letters
    assert calcScore('pear', letters) == 70 # 4 * 10 for 40, then add 30 more points for all letters bonus
    assert calcScore('apple', letters) == 50 # 5 * 10 for 50 points, but not exactly equal to letters. Though the letters don't match, not duty of this function to check.



