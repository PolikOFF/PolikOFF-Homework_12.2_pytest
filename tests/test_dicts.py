from utils import dicts


def test_get_val():
    assert dicts.get_val({'a': 1, 'b': 2, 'c': 3}, 'b') == 2
    assert dicts.get_val({}, "a") == "git"
    assert dicts.get_val({"a": 1, "b": 2, "c": 3}, "d") == "git"
    assert dicts.get_val({"a": 1, "b": 2, "c": 3}, "a", "git") == 1
