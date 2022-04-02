def double_affine_x_only(x1, A):
    """
    x-only doubling for the Montgomery ladder on E: B*y^2 = x^3 + A*x^2 + x

    INPUT:
    - `x1`: x-coordinate of point P in affine coordinates (x1, y1, 1)
    - `A`: curve coefficient: B*y^2 = x^3 + A*x^2 + x

    RETURN: x2 the x-coordinate of [2]P

    formula: 4*x1*x3*(x1**2 + A*x1 + 1) = (x1**2 - 1)**2
    """
    x2 = ( (x1**2 - 1)**2) / (4*x1*(x1**2 + A*x1 + 1))
    return x2