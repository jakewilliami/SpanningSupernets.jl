<h1 align="center">SpanningSupernet.jl</h1>

<!-- [![Stable](https://img.shields.io/badge/docs-stable-blue.svg)](https://jakewilliami.github.io/SpanningSupernet.jl/stable) -->
[![Dev](https://img.shields.io/badge/docs-dev-blue.svg)](https://jakewilliami.github.io/SpanningSupernet.jl/dev)
[![CI](https://github.com/jakewilliami/SpanningSupernet.jl/actions/workflows/CI.yml/badge.svg?branch=master)](https://github.com/jakewilliami/SpanningSupernet.jl/actions/workflows/CI.yml?query=branch%3Amaster)
[![Code Style: Blue](https://img.shields.io/badge/code%20style-blue-4495d1.svg)](https://github.com/invenia/BlueStyle)

This library provides an algorithm, via the `spanning_supernet` function, to calculate the minimal spanning supernet of a set of IPs such that all given IPs fall within that network.

## Quick Start

```julia
julia> using Sockets, SpanningSupernets

julia> spanning_supernet([ip"20.171.207.220", ip"20.171.207.211", ip"20.171.207.226", ip"20.171.207.239"])
IPv4Net("20.171.207.192/26")
```

## Citation

If your research depends on SpanningSupernet.jl, please consider giving us a formal citation: [`citation.bib`](./citation.bib).
