import pytest
from fib import fibonacci

class TestFib:
    
    def test_fib(self):
        assert fibonacci(5) == 5

    def test_fib(self):
        assert fibonacci(20) == 6765