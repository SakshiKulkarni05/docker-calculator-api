# conftest.py — tells pytest to add the project root to sys.path
# This allows `from main import app` to work inside tests/
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
