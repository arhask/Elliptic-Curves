
def montgomery_ladder_affine_x_only(m, P, A):
    """
    Montgomery ladder in affine coordinates

    INPUT:
    - `m`: scalar (integer)
    - `P`: point in projective coordinates (X, Y, Z)
    - `A`: curve coefficient
    """
    if m == 0:
        return (0, 0)
    if m < 0:
        m = -m
    mbits = ZZ(m).bits()
    n =len(mbits)

    xP= P[0]
    x0, x1 = xP, double_affine_x_only(xP, A)

    for i in range(n-2, -1, -1):
        if mbits[i] == 0:
            x0, x1 = double_affine_x_only(x0, A), add_affine_x_only(x0, x1, xP)
        else: 
            x0, x1 = add_affine_x_only(x0, x1, xP), double_affine_x_only(x1, A)
    return x0