def square(a: float) -> float:
    if not isinstance(a, float):
        raise TypeError
    return a*a