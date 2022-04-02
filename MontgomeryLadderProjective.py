def montgomery_ladder_proj_xz_only(m, P, A):
    """
    Montgomery ladder in projective coordinates

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
    n = len(mbits)

    xP, zP, = P[0], P[2]
    x0, z0 = xP, zP
    x1, z1 = double_proj_xz_only(x0, z0, A)

    for i in range(n-2, -1, -1):
        if mbits[i] == 0:
            x1, z1 = add_proj_xz_only(x0, z0, x1, z1, xP, zP)
            x0, z0 = double_proj_xz_only(x0, z0, A)
            
        else:
            x0, z0 = add_proj_xz_only(x0, z0, x1, z1, xP, zP)
            x1, z1 = double_proj_xz_only(x1, z1, A)

    return (x0, z0)
