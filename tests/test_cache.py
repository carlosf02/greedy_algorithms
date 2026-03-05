# tests/test_cache.py
# Unit tests for cache eviction policies.
# Add test cases here as you implement each policy.

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import fifo, lru, optff


# ---------------------------------------------------------------------------
# FIFO Tests
# ---------------------------------------------------------------------------

def test_fifo_basic():
    # TODO: add assertions once fifo() is implemented
    pass


# ---------------------------------------------------------------------------
# LRU Tests
# ---------------------------------------------------------------------------

def test_lru_basic():
    # TODO: add assertions once lru() is implemented
    pass


# ---------------------------------------------------------------------------
# OPTFF Tests
# ---------------------------------------------------------------------------

def test_optff_basic():
    # TODO: add assertions once optff() is implemented
    pass


# ---------------------------------------------------------------------------
# Comparative Tests
# ---------------------------------------------------------------------------

def test_optff_leq_lru_fifo():
    """OPTFF should never have MORE misses than LRU or FIFO."""
    # TODO: run all three on multiple sequences and assert optff <= others
    pass
