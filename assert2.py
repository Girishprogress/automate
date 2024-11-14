import pytest

def test_exception():
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0

def test_approx():
    assert 0.1 + 0.2 == pytest.approx(0.3)

def dependent(x):
    return x*55*60 
   