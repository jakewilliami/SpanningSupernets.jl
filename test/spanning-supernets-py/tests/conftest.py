from dataclasses import dataclass
from ipaddress import IPv4Address, IPv4Network

import pytest

# Pytest suggests defining all fixtures within a single conftest.py file:
#   gist.github.com/peterhurford/09f7dcda0ab04b95c026c60fa49c2a68


@dataclass
class MockIPRange:
    list: list[IPv4Address]
    expected: IPv4Network


@pytest.fixture
def range1() -> MockIPRange:
    yield MockIPRange(
        list=[
            IPv4Address("20.171.207.220"),
            IPv4Address("20.171.207.211"),
            IPv4Address("20.171.207.226"),
            IPv4Address("20.171.207.239"),
        ],
        expected=IPv4Network("20.171.207.192/26"),
    )


@pytest.fixture
def range2() -> MockIPRange:
    yield MockIPRange(
        list=[
            IPv4Address("192.168.1.1"),
            IPv4Address("192.168.1.2"),
            IPv4Address("192.168.1.3"),
            IPv4Address("192.168.1.10"),
            IPv4Address("192.168.1.11"),
            IPv4Address("192.168.1.20"),
        ],
        expected=IPv4Network("192.168.1.0/27"),
    )


@pytest.fixture
def range3() -> MockIPRange:
    yield MockIPRange(
        list=[
            IPv4Address("163.7.135.135"),
            IPv4Address("163.7.135.152"),
            IPv4Address("163.7.135.153"),
            IPv4Address("163.7.135.154"),
            IPv4Address("163.7.135.155"),
            IPv4Address("163.7.135.156"),
            IPv4Address("163.7.135.159"),
            IPv4Address("163.7.135.143"),
            IPv4Address("163.7.135.22"),
            IPv4Address("163.7.135.36"),
            IPv4Address("163.7.135.99"),
            IPv4Address("163.7.135.142"),
            IPv4Address("163.7.135.157"),
            IPv4Address("163.7.135.105"),
            IPv4Address("163.7.135.2"),
            IPv4Address("163.7.135.32"),
            IPv4Address("163.7.135.71"),
            IPv4Address("163.7.135.72"),
            IPv4Address("163.7.135.100"),
            IPv4Address("163.7.135.107"),
            IPv4Address("163.7.135.127"),
            IPv4Address("163.7.135.141"),
            IPv4Address("163.7.135.39"),
            IPv4Address("163.7.135.42"),
            IPv4Address("163.7.135.47"),
            IPv4Address("163.7.135.88"),
            IPv4Address("163.7.135.89"),
            IPv4Address("163.7.135.90"),
            IPv4Address("163.7.135.158"),
            IPv4Address("163.7.135.46"),
            IPv4Address("163.7.135.53"),
            IPv4Address("163.7.135.56"),
            IPv4Address("163.7.135.62"),
            IPv4Address("163.7.135.66"),
            IPv4Address("163.7.135.94"),
            IPv4Address("163.7.135.1"),
            IPv4Address("163.7.135.128"),
            IPv4Address("163.7.135.139"),
            IPv4Address("163.7.135.14"),
            IPv4Address("163.7.135.140"),
            IPv4Address("163.7.135.3"),
            IPv4Address("163.7.135.38"),
            IPv4Address("163.7.135.48"),
            IPv4Address("163.7.135.54"),
            IPv4Address("163.7.135.61"),
            IPv4Address("163.7.135.67"),
            IPv4Address("163.7.135.73"),
            IPv4Address("163.7.135.93"),
            IPv4Address("163.7.135.96"),
            IPv4Address("163.7.135.101"),
            IPv4Address("163.7.135.104"),
            IPv4Address("163.7.135.125"),
            IPv4Address("163.7.135.26"),
            IPv4Address("163.7.135.31"),
            IPv4Address("163.7.135.5"),
            IPv4Address("163.7.135.59"),
            IPv4Address("163.7.135.69"),
            IPv4Address("163.7.135.102"),
            IPv4Address("163.7.135.11"),
            IPv4Address("163.7.135.121"),
            IPv4Address("163.7.135.13"),
            IPv4Address("163.7.135.131"),
            IPv4Address("163.7.135.133"),
            IPv4Address("163.7.135.24"),
            IPv4Address("163.7.135.28"),
            IPv4Address("163.7.135.30"),
            IPv4Address("163.7.135.43"),
            IPv4Address("163.7.135.63"),
            IPv4Address("163.7.135.7"),
            IPv4Address("163.7.135.74"),
            IPv4Address("163.7.135.12"),
            IPv4Address("163.7.135.126"),
            IPv4Address("163.7.135.130"),
            IPv4Address("163.7.135.132"),
            IPv4Address("163.7.135.134"),
            IPv4Address("163.7.135.15"),
            IPv4Address("163.7.135.17"),
            IPv4Address("163.7.135.23"),
            IPv4Address("163.7.135.25"),
            IPv4Address("163.7.135.27"),
            IPv4Address("163.7.135.34"),
            IPv4Address("163.7.135.40"),
            IPv4Address("163.7.135.44"),
            IPv4Address("163.7.135.49"),
            IPv4Address("163.7.135.50"),
            IPv4Address("163.7.135.52"),
            IPv4Address("163.7.135.58"),
            IPv4Address("163.7.135.6"),
            IPv4Address("163.7.135.64"),
            IPv4Address("163.7.135.68"),
            IPv4Address("163.7.135.9"),
            IPv4Address("163.7.135.98"),
            IPv4Address("163.7.135.0"),
            IPv4Address("163.7.135.129"),
            IPv4Address("163.7.135.138"),
            IPv4Address("163.7.135.16"),
            IPv4Address("163.7.135.21"),
            IPv4Address("163.7.135.29"),
            IPv4Address("163.7.135.55"),
            IPv4Address("163.7.135.57"),
            IPv4Address("163.7.135.60"),
            IPv4Address("163.7.135.8"),
            IPv4Address("163.7.135.91"),
            IPv4Address("163.7.135.95"),
            IPv4Address("163.7.135.122"),
            IPv4Address("163.7.135.136"),
            IPv4Address("163.7.135.18"),
            IPv4Address("163.7.135.19"),
            IPv4Address("163.7.135.33"),
            IPv4Address("163.7.135.35"),
            IPv4Address("163.7.135.37"),
            IPv4Address("163.7.135.41"),
            IPv4Address("163.7.135.65"),
            IPv4Address("163.7.135.70"),
            IPv4Address("163.7.135.75"),
            IPv4Address("163.7.135.97"),
            IPv4Address("163.7.135.10"),
            IPv4Address("163.7.135.106"),
            IPv4Address("163.7.135.123"),
            IPv4Address("163.7.135.124"),
            IPv4Address("163.7.135.137"),
            IPv4Address("163.7.135.20"),
            IPv4Address("163.7.135.4"),
            IPv4Address("163.7.135.45"),
            IPv4Address("163.7.135.120"),
            IPv4Address("163.7.135.103"),
            IPv4Address("163.7.135.51"),
            IPv4Address("163.7.135.92"),
        ],
        expected=IPv4Network("163.7.135.0/24"),
    )
