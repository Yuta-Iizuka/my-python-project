def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

# 成功テスト
def test_success_example():
    assert 2 * 3 == 6

# 失敗テスト（前回の失敗テスト）
def test_fail_example():
    assert 1 + 1 == 3