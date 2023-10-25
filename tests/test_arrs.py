from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([10,20,-1], 2, "test") == -1
    assert arrs.get([10,20,-1],-1, "test") == "test"
    assert arrs.get([], 0, default="Empty") == "Empty"
    assert arrs.get([1, 2, 3, 4, 5], 3) == int("4")

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([3, 14, 28], 0, 1) == [3]
    assert arrs.my_slice([-2, 13, 51,100], 1, 3) == [13,51]
    assert arrs.my_slice([2, 6, -1], 0, 1) == [2]
    assert arrs.my_slice([2, 6, -1], 0, 1) == [2]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=2) == [1, 2]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=-3, end=-2) == [3]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=-5, end=5) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3, 4, 5]) != []

