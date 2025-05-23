"""Stub for when Cython is not available."""

from __future__ import annotations


class FakeCython:
    """Stub for when Cython is not available."""

    @property
    def compiled(self) -> bool:
        return False


FAKE_CYTHON = FakeCython()
