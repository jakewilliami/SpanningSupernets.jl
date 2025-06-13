import ipaddress
from ipaddress import IPv4Address, IPv4Network


def parse_ip_list(ips: list[str], validate: bool = True) -> list[IPv4Address] | None:
    if len(ips) < 2:
        print("ERROR: Cannot compute for less than two input IPs")
        return None

    ip_objects = sorted(ipaddress.ip_address(ip) for ip in ips)

    if validate and not all(isinstance(ip, IPv4Address) for ip in ip_objects):
        print("ERROR: Not all IPs are IPv4s")
        return None

    return ip_objects


def _calculate_supernet_internal(ips: list[IPv4Address]) -> IPv4Network | None:
    i0, i1 = ips[0], ips[-1]
    n0, n1 = int(i0), int(i1)

    for prefixlen in range(32, -1, -1):
        network = ipaddress.ip_network((i0, prefixlen), strict=False)
        if int(network.network_address) <= n0 and int(network.broadcast_address) >= n1:
            return network

    print(f"ERROR: should never get here ({network})")
    return None


# TODO: raise ValueErrors in case this is used in a program rather than a CLI?
def calculate_supernet(ips: list[IPv4Address], verify: bool = True) -> IPv4Network | None:
    ip_objects = parse_ip_list(ips)
    if not ip_objects:
        return None

    network = _calculate_supernet_internal(ip_objects)
    if not network:
        return None

    # Sanity check: not good for performance but this Python application is
    # only really for unit testing and confirming that I know how this process
    # works, so it's very good to be sure.
    #
    # The primary thing we do is check network completeness (i.e., all IPs in the
    # input are duly in this network,
    #
    # I previously had an alternative method of calculation but this turned out
    # to be inacurate, so we do not verify the answer with a different calculation.
    # The previous step should be sufficient.
    if verify and not all(ip in network for ip in ip_objects):
        print(f"ERROR [SANITY CHECK]: Not all IPs are in the range {network!r}")
        return None

    return network
