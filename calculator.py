def addition(a: int, b: int) -> int:
    """Fonction d'addition.

    Args:
        a (int): Premier opérande.
        b (int): Deuxième opérande.

    Returns:
        int: Résultat de l'addition.
    """
    result = a + b
    return result

def soustraction(a: int, b: int) -> int:
    """Fonction de soustraction.

    Args:
        a (int): Premier opérande.
        b (int): Deuxième opérande.

    Returns:
        int: Résultat de la soustraction.
    """
    result = a - b
    return result

def division(a: int, b: int) -> float:
    """Fonction de division.

    Args:
        a (int): Dividende.
        b (int): Diviseur.

    Returns:
        float: Résultat de la division si le diviseur n'est pas zéro, sinon renvoie un message d'erreur.
    """
    if b != 0:
        result = a / b
        return result
    return "Division impossible par 0"  # Suppression de l'else après le return
