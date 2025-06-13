from ipaddress import IPv4Network

from spanning_supernet import calculate_supernet


def test_range1(range1: list[str]):
    assert calculate_supernet(range1) == IPv4Network("20.171.207.192/26")


def test_range2(range2: list[str]):
    assert calculate_supernet(range2) == IPv4Network("192.168.1.0/27")


def test_range3(range3: list[str]):
    assert calculate_supernet(range3) == IPv4Network("163.7.135.0/24")
