def double_proj_xz_only(X1, Z1, A):
    """
    Doubling in projective (X,Z)-coordinates on a Montgomery curve E: B*Y^2*Z = X^3 + A*X^2*Z + X*Z^2

    INPUT:
    - `X1`, `Z1`: point P in projective (X,Z)-coordinates (X1, Z1), if Z1 = 0 the point is at infinity
    - `A`: curve coefficient: B*y^2 = x^3 + A*x^2 + x

    RETURN: (X2,Z2) the (X,Z)-coordinates of [2]P

    x3 = (x1**2 - 1)**2/(4*x1*(x1**2 + A*x1 + 1))
    X3/Z3 = TODO
    if the point is a 2-torsion point (0,0,1) or (a,0,1) it will return (0,0) in (X,Z)
    """
    if Z1 == 0 or X1 == 0:
        return (0, 0)

    X3 = (X1^2 - Z1^2)^2
    Z3 = 4*X1*Z1*(X1^2 + A*X1*Z1 + Z1^2)
    return (X3, Z3)