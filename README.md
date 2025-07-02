<h1 align="center">SpanningSupernets.jl</h1>

<!-- [![Stable](https://img.shields.io/badge/docs-stable-blue.svg)](https://jakewilliami.github.io/SpanningSupernets.jl/stable) -->
[![Dev](https://img.shields.io/badge/docs-dev-blue.svg)](https://jakewilliami.github.io/SpanningSupernets.jl/dev)
[![CI](https://github.com/jakewilliami/SpanningSupernets.jl/actions/workflows/CI.yml/badge.svg?branch=master)](https://github.com/jakewilliami/SpanningSupernets.jl/actions/workflows/CI.yml?query=branch%3Amaster)
[![Code Style: Blue](https://img.shields.io/badge/code%20style-blue-4495d1.svg)](https://github.com/invenia/BlueStyle)

This library provides an algorithm, via the `spanning_supernet` function, to calculate the minimal spanning supernet of a set of IPs such that all given IPs fall within that network.

## Quick Start

```julia-repl
julia> using Sockets, SpanningSupernets

julia> spanning_supernet([ip"20.171.207.220", ip"20.171.207.211", ip"20.171.207.226", ip"20.171.207.239"])
IPv4Net("20.171.207.192/26")
```

## Development

Ensure you have both [UV](https://github.com/astral-sh/uv) and [Just](https://github.com/casey/just).

To run unit tests, simply run:

```commandline
$ just test
# ...
```

I am using an [independent Python version of this library](./tests/spanning-supernets-py/) for testing.  This way, I know the Julia library works the same way that a library written with a different backend does.  It allows us to be doubly sure that the outcome is correct.

We also use UV to conveniently run pre-commit:

```commandline
$ just fmt
```

In order to commit, you will want to ensure pre-commits are installed:

```commandline
$ uvx pre-commit install
```

## Citation

If your research depends on SpanningSupernets.jl, please consider giving us a formal citation: [`citation.bib`](./citation.bib).
