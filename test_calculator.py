from calculator import Calculator

calculator = Calculator()


def test_add():
    a = 2
    b = 3
    expected_result = 6
    result = calculator.add(a, b)
    assert result == expected_result, f"Expected: {expected_result}, but got: {result}"
