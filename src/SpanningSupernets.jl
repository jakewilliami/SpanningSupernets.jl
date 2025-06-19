module SpanningSupernets

export spanning_supernet

using Sockets, IPNets

# Check if prospective network is valid; adapted from
#   github.com/JuliaWeb/IPNets.jl/blob/92a9364b/src/IPNets.jl#L36-L58
#   github.com/python/cpython/blob/3cb10979/Lib/ipaddress.py#L1537-L1538
function Base.isvalid(::Type{IPv4Net}, network::Tuple{IPv4, Integer})
    # Extract netaddr and netmask
    netaddr₀, prefix_length = network
    netaddr = netaddr₀.host
    netmask = IPNets.to_mask(UInt32(prefix_length))

    # Verify that host bits do not get set
    netaddr′ = netaddr & netmask
    return netaddr′ === netaddr
end

# Constructor for IPv4Net, adapted with strict=False logic from Python's ipaddress:
#   github.com/python/cpython/blob/3cb10979/Lib/ipaddress.py#L1535-L1543
function ipv4_network(netaddr::IPv4, prefix_length::UInt32)
    # Base case: network is well defined, with no host bits set
    isvalid(IPv4Net, (netaddr, prefix_length)) && return IPv4Net(netaddr, prefix_length)

    # Case two: non-strict fallback handling with unusual network address.
    #
    # If the network is not valid, then we have to handle that as we do in the
    # ipaddress Python library, with strict=False.  This ignores the requirement
    # that a network address that has been passed is a true network address (e.g.,
    # 192.168.1.0/24); rather, we allow it to be an IP address on a network (e.g.,
    # 192.168.1.1/24), thus having host bits set in the network portion of the
    # address.  The correctness of the CIDR notation is defined in RFC 4632, which
    # I have not read:
    #   datatracker.ietf.org/doc/html/rfc4632
    #
    # TODO: Although we have reproduced the seemingly working product initially
    # written in Python, I would like to adapt this to not use this strict=False
    # workflow.  Instead, we should surely find a proper network address to use
    # in order to reach our desired outcome.  This would surely be more accurate
    #
    # In order to allow the input to construct a network, we should find a more
    # accurate netmask and network address to use.  We first must calculate netmask
    # using IPNet's internal function; similar to the equivalent process in Python's
    # ipaddress library:
    #   github.com/python/cpython/blob/3cb10979/Lib/ipaddress.py#L1156-L1180
    #   github.com/python/cpython/blob/3cb10979/Lib/ipaddress.py#L426-L437
    #
    # Alternatively, we could have written our own to_mask function:
    #
    #     function to_mask(a::UInt32)
    #         b = 2^32 - 1
    #         return IPv4(b ⊻ (b >> a))
    #     end
    netmask = IPv4(IPNets.to_mask(prefix_length))

    #
    netaddr = IPv4(UInt32(netaddr) & UInt32(netmask))
    return IPv4Net(netaddr, netmask)
end

# Calculate broadcast address; adapted from
#   https://github.com/python/cpython/blob/3cb10979/Lib/ipaddress.py#L753-L760
hostmask(net::IPv4Net)::UInt32 = net.netmask ⊻ (2^32 - 1)
broadcastaddr(net::IPv4Net)::UInt32 = net.netaddr | hostmask(net)

# Calculate *the* minimal spanning supernet
#
# TODO: it may be convenient for users for this function to return a *list* of
# networks, in the case that all IPs provided to not fit nicely into one range,
# such that there are multiple spanning networks but we prioritise fewer networks.
function spanning_supernet(ips::Vector{IPv4})
    i₀, i₁ = extrema(ips)
    n₀, n₁ = UInt32(i₀), UInt32(i₁)

    for prefix_length in 32:-1:0
        network = ipv4_network(i₀, UInt32(prefix_length))

        network.netaddr ≤ n₀ && n₁ ≤ broadcastaddr(network) && return network
    end

    return error("It may be impossible to calculate a supernet with all given IPs.  Please submit a bug report.",)
end

end
