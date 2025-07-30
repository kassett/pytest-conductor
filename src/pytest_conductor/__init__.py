"""Pytest plugin for coordinating the order in which marked tests run."""

VERSION = "0.1.1"

# Import hooks to register them with pytest
from . import hooks  # noqa
