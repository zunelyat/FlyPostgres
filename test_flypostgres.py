# test_flypostgres.py
"""
Tests for FlyPostgres module.
"""

import unittest
from flypostgres import FlyPostgres

class TestFlyPostgres(unittest.TestCase):
    """Test cases for FlyPostgres class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FlyPostgres()
        self.assertIsInstance(instance, FlyPostgres)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FlyPostgres()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
