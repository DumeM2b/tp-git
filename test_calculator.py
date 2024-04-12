"""
Module test_calculator
"""

from calculator import addition, soustraction, division

def test_addition():
    """Test de la fonction d'addition."""
    assert addition(1, 2) == 3

def test_soustraction():
    """Test de la fonction de soustraction."""
    assert soustraction(2, 1) == 1

def test_division():
    """Test de la fonction de division."""
    assert division(6, 3) == 2.0
    assert division(6, 0) == "Division impossible par 0"
