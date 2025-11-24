from src.math_operations import add, subtract, multiply, divide, power, modulus, floor_divide, square_root, logarithm, factorial
import pytest

def test_add():
    assert add(2, 3) == 5 # Assert means check if the result is as expected
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1

def test_multiply():
    assert multiply(4, 2) == 8
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(6, 2) == 3
    with pytest.raises(ValueError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_modulus():
    assert modulus(10, 3) == 1
    assert modulus(14, 5) == 4
def test_floor_divide():
    assert floor_divide(7, 2) == 3
    with pytest.raises(ValueError):
        floor_divide(5, 0)
def test_square_root():
    assert square_root(16) == 4
    with pytest.raises(ValueError):
        square_root(-4)
def test_logarithm():
    assert logarithm(100, 10) == 2
    with pytest.raises(ValueError):
        logarithm(-10)

def test_factorial():
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-3)
    assert factorial(0) == 1
    assert factorial(1) == 1

# if __name__ == "__main__":
#     pytest.main()