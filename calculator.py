def addition(a: int, b: int) -> int:
    """Addition function.

    Args:
        a (int): First operand.
        b (int): Second operand.

    Returns:
        int: Result of the addition.
    """
    result = a + b
    return result

def soustraction(a: int, b: int) -> int:
    """Subtraction function.

    Args:
        a (int): First operand.
        b (int): Second operand.

    Returns:
        int: Result of the subtraction.
    """
    result = a - b
    return result

def division(a: int, b: int) -> float:
    """Division function.

    Args:
        a (int): Dividend.
        b (int): Divisor.

    Returns:
        float: Result of the division if divisor is not zero, otherwise returns an error message.
    """
    if b != 0:
        result = a / b
        return result
    else:
        return "Impossible division by 0"
