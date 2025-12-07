# geometry.py


def square_area(side_length: float) -> float:
    """
    Calculate the area of a square.

    Args:
    - side_length (float): the length of one side of the square.

    Returns:
    - float: the area of the square.
    """
    # Write here your code
    if isinstance(side_length, int) != True and isinstance(side_length, float) != True:
        raise TypeError("El parametre d'entrada no es un numero")
    # area de un quadrat algoritme area = costat * costat
    return (side_length * side_length)    
    pass


def rectangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
    - base_length (float): the length of the base of the rectangle.
    - height (float): the height of the rectangle.

    Returns:
    - float: the area of the rectangle.
    """
    # Write here your code
    if isinstance(base_length, int) != True and isinstance(base_length, float) != True:
        raise TypeError("El parametre d'entrada base no es un numero")
    if isinstance(height, int) != True and isinstance(height, float) != True:
        raise TypeError("El parametre d'entrada alçada no es un numero")
    # Algoritme area = base * alçada
    return (height * base_length)
    pass


def triangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Args:
    - base_length (float): the length of the base of the triangle.
    - height (float): the height of the triangle.

    Returns:
    - float: the area of the triangle.
    """
    # Write here your code
    if isinstance(base_length, int) != True and isinstance(base_length, float) != True and base_length>0:
        raise TypeError("El parametre d'entrada base no es un numero positiu diferent de zero")
    if isinstance(height, int) != True and isinstance(height, float) != True and height>0:
        raise TypeError("El parametre d'entrada alçada no es un numero positiu diferent de zero")    
    # Algoritme = base * alçada /2
    return (base_length * height / 2)
    pass


def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
    - radius (float): the radius of the circle.

    Returns:
    - float: the area of the circle
    """
    # Write here your code
    if isinstance(radius, int) != True and isinstance(radius, float) != True and radius>0:
        raise TypeError("El parametre d'entrada base no es un numero positiu diferent de zero")
    
    return (3.14159 * radius * radius)
    pass
