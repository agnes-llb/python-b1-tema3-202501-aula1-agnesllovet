# archivo ej3a1_operations.py


def add(num_1: float, num_2: float) -> float:
    # Write here your code
    if isinstance(num_1, float) != True and isinstance(num_1, int)!= True:
        raise TypeError ("Els primer operant entrats no es un numero")
    if isinstance(num_2, float) != True and isinstance(num_2, int)!= True:
        raise TypeError ("Els segon operant entrats no es un numero")   
    return (num_1 + num_2)
    pass


def subtract(num_1: float, num_2: float) -> float:
    # Write here your code
    if isinstance(num_1, float) != True and isinstance(num_1, int)!= True:
        raise TypeError ("Els primer operant entrats no es un numero")
    if isinstance(num_2, float) != True and isinstance(num_2, int)!= True:
        raise TypeError ("Els segon operant entrats no es un numero")
    return (num_1 - num_2)   
    pass


def multiply(num_1: float, num_2: float) -> float:
    # Write here your code
    if isinstance(num_1, float) != True and isinstance(num_1, int)!= True:
        raise TypeError ("Els primer operant entrats no es un numero")
    if isinstance(num_2, float) != True and isinstance(num_2, int)!= True:
        raise TypeError ("Els segon operant entrats no es un numero")
    return (num_1 * num_2)
    pass


def divide(num_1: float, num_2: float) -> float:
    # Write here your code
    if isinstance(num_1, float) != True and isinstance(num_1, int)!= True:
        raise TypeError ("Els primer operant entrats no es un numero")
    if isinstance(num_2, float) != True and isinstance(num_2, int)!= True and num_2 == 0:
        raise TypeError ("Els segon operant entrats no es un numero or es zero")
    return (num_1 / num_2)
    pass
