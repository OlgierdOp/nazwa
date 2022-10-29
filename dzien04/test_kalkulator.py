from kalkulator_funkcje import add
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(-5, -10) == -15
    assert add(10, 0) == 10
