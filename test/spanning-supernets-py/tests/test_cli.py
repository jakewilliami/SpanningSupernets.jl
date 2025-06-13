from ipaddress import IPv4Address, IPv4Network
from subprocess import CalledProcessError, CompletedProcess, run

from conftest import MockIPRange

# CLI/Integration tests, adapted from (using subprocess in the interest of simplicity):
#   stackoverflow.com/a/70888702


def run_cli(ips: list[IPv4Address]) -> CompletedProcess | CalledProcessError:
    ips = [str(ip) for ip in ips]
    args = ["uv", "run", "supnet", *ips]
    return run(args, check=True, capture_output=True, text=True)


def check_cli(test_data: MockIPRange):
    try:
        res = run_cli(test_data.list)
        assert res.returncode == 0

        ans = IPv4Network(res.stdout.strip())
        assert ans == test_data.expected

        for ip in test_data.list:
            assert ip in ans

    except CalledProcessError as err:
        assert res.returncode == 0  # this should fail
        raise err


def test_range1(range1: MockIPRange):
    check_cli(range1)


def test_range2(range2: MockIPRange):
    check_cli(range2)


def test_range3(range3: MockIPRange):
    check_cli(range3)
