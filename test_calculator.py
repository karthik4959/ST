from calculator import Calculator

calculator = Calculator()


def test_add(a, b, expected_result):
    result = calculator.add(a, b)
    if result == expected_result:
        print("Addition test passed")
    else:
        raise ValueError("Addition test failed. Expected:", expected_result, "but got:", result)


test_add(2, 3, 55)
