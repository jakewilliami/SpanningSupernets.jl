import argparse

from spanning_supernet import calculate_supernet


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="supnet",
        description="Calculate spanning supernets in Python for independent integration testing purposes",
    )

    parser.add_argument("ips", nargs="*")

    return parser.parse_args()


def run_main(*, ips: list[str]) -> int:
    network = calculate_supernet(ips)

    if not network:
        return 1

    print(network)
    return 0


def main():
    opts = vars(parse_args())
    raise SystemExit(run_main(**opts))
