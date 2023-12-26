# test_math_functions.py
import math_functions
import pytest


test_cases = [
    ((2, 3), 5),
    ((1, -1), 0),
    ((1, "-1"), TypeError)
]


@pytest.mark.parametrize("test_case, result", test_cases)
def test_add(test_case, result):
    try:
        assert math_functions.add(*test_case) == result
    except Exception as error:
        assert type(error) == result


test_cases = [
    ((2, 3), -1),
    ((1, -1), 2),
    ((1, "-1"), TypeError)
]


@pytest.mark.parametrize("test_case, result", test_cases)
def test_subtract(test_case, result):
    try:
        assert math_functions.subtract(*test_case) == result
    except Exception as error:
        assert type(error) == result


test_cases = [
    ((2, 3), 6),
    ((1, "-1"), "-1"),
    (({}, []), TypeError)
]


@pytest.mark.parametrize("test_case, result", test_cases)
def test_multiply(test_case, result):
    try:
        assert math_functions.multiply(*test_case) == result
    except Exception as error:
        assert type(error) == result


test_cases = [
    ((3, 3), 1),
    ((1, 0), ValueError),
    ((1, "-1"), TypeError)
]


@pytest.mark.parametrize("test_case, result", test_cases)
def test_divide(test_case, result):
    try:
        assert math_functions.divide(*test_case) == result
    except Exception as error:
        assert type(error) == result