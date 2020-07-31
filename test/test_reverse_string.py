from reverse_string.reverse_string import reverse
import copy

def test_inplace_reverse():
    test_param = ["a", "b", "c", "d", "e", "f"]
    prepared_param = copy.copy(test_param)
    reverse(test_param)

    assert prepared_param[::-1] == test_param