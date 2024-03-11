from calculator import Calculator

calculator = Calculator()


def test_add():
    a = 2
    b = 3
    expected_result = 5
    result = calculator.add(a, b)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"

def test_sub():
    a = 5
    b = 2
    expected_result = 3
    result = calculator.subtract(a, b)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}" 

def test_mult():
    a = 5
    b = 2
    expected_result = 10
    result = calculator.multiply(a, b)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"

def test_div():
    a = 4
    b = 2
    expected_result = 2
    result = calculator.divide(a, b)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"