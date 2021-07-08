import pytest
from main import fib

class TestFib:
    
    def test_fib(self):
        assert fib(20) == 6765