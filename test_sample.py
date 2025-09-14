def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

def test_fail_example():
    assert 1 + 1 == 3  # わざと間違ったテスト
    