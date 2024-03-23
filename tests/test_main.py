# tests/test_main.py

import pytest
from src.stock_analysis_program import main

def test_main_exists():
    assert main is not None, "Main module should exist."
