from quick_calc.calculator import Calculator

def test_full_user_flow():
    calc = Calculator()
    result = calc.add(5, 3)
    assert result == 8

def test_clear_function():
    calc = Calculator()
    calc.add(10, 5)
    assert calc.clear() == 0