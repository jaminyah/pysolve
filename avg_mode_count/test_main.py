import pytest
from main import countChars

class TestCountChars:

    def test_count_chars(self):
        input = "This is Pythoni world!"

        assert countChars(input) == ('i', 3, 1.3157894736842106)