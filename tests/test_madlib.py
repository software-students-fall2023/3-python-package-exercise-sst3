import pytest
from src.sstgame import madlib
class Tests:

    @pytest.fixture
    def test_first(self):
        assert 3 == 3
    # def test_ReadTextSize():
    #     prompts = readText("text.txt")
    #     assert(len(prompts) == 3)
