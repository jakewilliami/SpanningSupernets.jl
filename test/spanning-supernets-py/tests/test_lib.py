from conftest import MockIPRange

from spanning_supernets import calculate_supernet


def test_range1(range1: MockIPRange):
    assert calculate_supernet(range1.list) == range1.expected


def test_range2(range2: MockIPRange):
    assert calculate_supernet(range2.list) == range2.expected


def test_range3(range3: MockIPRange):
    assert calculate_supernet(range3.list) == range3.expected
