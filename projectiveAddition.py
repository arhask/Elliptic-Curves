def add_proj_xz_only(X1, Z1, X2, Z2, X4, Z4):
    """
    Addition in Projective X,Z-only on a Montgomery curve E: B*Y^2*Z = X^3 + A*X^2*Z + X*Z^2

    INPUT:
    - `X1`, `Z1`: point P in projective (X,Z)-coordinates (X1, Z1), if Z1 = 0 the point is at infinity
    - `X2`, `Z2`: point R in projective (X,Z)-coordinates (X2, Z2), if Z2 = 0 the point is at infinity
    - `X4`, `Z4`: point P-R in projective (X,Z)-coordinates (X4, Z4), if Z4 = 0 the point is at infinity

    RETURN: (X3, Z3) = R+P in projective (X,Z)-coordinates
    Source: http://www.hyperelliptic.org/EFD/g1p/auto-montgom-xz.html#diffadd-dadd-1987-m
    
    """
    if Z1 == 0 and Z2 == 0:
        return (0, 0) # corresponds to (0, 1, 0) in full (X, Y, Z) coordinates
    if Z1 == 0:
        return (X2, Z2)
    if Z2 == 0:
        return (X1, Z1)

    X3 = ((X1*X2 - Z1*Z2)^2) * Z4
    Z3 = ((X1*Z2 - X2*Z1)^2) * X4

    return (X3, Z3)