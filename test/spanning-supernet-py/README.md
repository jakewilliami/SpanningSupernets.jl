<h1 align="center">SpanningSupernet.py</h1>

The initial implementation of the algorithm by which minimal spanning supernets are calculated was drafted in Python.  As Julia has fewer of the conveniences that Python has, I wanted to be sure that the Julia library is doing everything correctly, albeit more manually.  As such, this sub-project is designed to be used as cross-validation for testing the Julia library.

## Quick Start

Ensure you have both [UV](https://github.com/astral-sh/uv) and [Just](https://github.com/casey/just).

### Run the CLI

```commandline
$ uv run supnet 20.171.207.220 20.171.207.211 20.171.207.226 20.171.207.239
20.171.207.192/26
```

### Run Unit Tests

```commandline
$ just test
# ...
```
