def add_affine_x_only(x1, x2, x4):
    """
    x-only addition for the Montgomery ladder on E: B*y^2 = x^3 + A*x^2 + x

    INPUT:
    - `x1`: x-coordinate of point P in affine coordinates (x1, y1, 1)
    - `x2`: x-coordinate of point Q in affine coordinates (x2, y2, 1)
    - `x4`: x-coordinate of point (P-Q) in affine coordinates (x4, y4, 1)

    RETURN: x3 the x-coordinate of (P+Q)

    formula: x3*x4*(x1 - x2)^2 = (x1*x2 - 1)^2
    The function assumes: x1 != x2, x1 or x2 non-zero, and x4 is non-zero.
    It does not test for the consistency of the inputs.
    """
    
    x3 = ((x1*x2 - 1)^2 ) / (x4*(x1 - x2)^2)
    return x3