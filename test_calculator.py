from calculator import addition, soustraction, division


def test_addition():
    """Test de la fonction addition."""
    assert addition(1, 2) == 3

def test_soustraction():
    """Test de la fonction soustraction."""
    assert soustraction(2, 1) == 1

def test_division():
    """Test de la fonction division."""
    assert division(2, 1) == 2
    assert division(4, 2) == 2
    # Ajoutez d'autres cas de test ici

# Exécution des tests unitaires
if __name__ == "__main__":
    test_addition()
    test_soustraction()
    test_division()
