import pytest
from functions import *


@pytest.mark.parametrize("document, res",[
    ('42514258', True),
    ('41254657', True),
    ('45147', False),
])
def test_dni_verification(document, res):
    assert dni_verification(document) == res


@pytest.mark.parametrize("string, res",[
    ('Hola', 'H o l a '),
    ('Adios', 'A d i o s '),
    ('Que', 'Q u e '),
])
def test_return_wh_spaces(string, res):
    assert return_wh_spaces(string) == res


@pytest.mark.parametrize("number, res", [
    (5, True),
    (4, False),
    (7, True),
])
def test_prime_number(number, res):
    assert prime_number(number) == res


@pytest.mark.parametrize("num, res", [
    (5, 120),
    (7, 5040),
    (3, 6)
])
def test_factorial(num, res):
    assert factorial(num) == res


