import main
import pytest

def test_suma():
    a=5
    b=13

    out=main.suma(a,b)
    assert out==18