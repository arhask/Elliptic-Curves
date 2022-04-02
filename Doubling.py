#Doubling a point P on the elliptic curve

#This time the slope l is found by calculating partial derivatives
L = E.derivative(X)(x_1,y_1)*(X-x_1) + E.derivative(Y)(x_1,y_1)*(Y-y_1)
print("partial f / partial x (x_1,y_1) = {}".format(E.derivative(X)(x_1,y_1)))
print("partial f / partial y (x_1,y_1) = {}".format(E.derivative(Y)(x_1,y_1)))
lambda_dbl = -L.coefficient({X:1})/L.coefficient({Y:1}); print("lambda_dbl = {}".format(lambda_dbl))

Lyl = l*(X-x_1) + y_1
Ly = lambda_dbl*(X-x_1) + y_1
Eq = E([X, Lyl]); print("E(X, value of Y in the langent L) = {}".format(Eq))

#-X^3 + (l^2 - a)*X^2 + (-2*l^2*x_1 + 2*l*y_1 - 1)*X + l^2*x_1^2 - 2*l*x_1*y_1 + y_1^2
assert QQx(Eq([x_1,y_1])) % QQx(E([x_1,y_1])) == 0
assert QQx(Eq % (X - x_1)) % E([x_1,y_1]) == 0

print("L intersects E has solutions Eq, and\nEq mod (X-x_1) = {} = {} mod E([x_1,y_1])".format(Eq % (X-x_1), (Eq % (X-x_1)) % E([x_1,y_1])))
assert (Eq % (X-x_1)) % E([x_1,y_1]) == 0
print("simplify Eq by X-x1")

#We apply the same logic, we divide the curve by the root we already know
Eq2 = Eq // (X-x_1) ; print("Eq2 = Eq // (X-x_1) = {}".format(Eq2))
Eq3 = Eq2 % (X-x_1); print("Eq3 = Eq2 mod (X-x_1) = {}".format(Eq3))
if Eq3 != 0:
    Eq4 = QQx(Eq3)([a,b,lambda_dbl,x_1,y_1,x_2,y_2])
    print("Eq3(l=lambda_dbl) = {}".format(Eq4))
    if Eq4 != 0:
        print("Eq4(l=lambda_dbl) % E([x_1,y_1]) = {}".format(Eq4 % QQx(E([x_1,y_1]))))

#-2*a*x_1 - 3*x_1^2 + 2*l*y_1 - 1
assert QQx(Eq3)([a,b,lambda_dbl,x_1,y_1,x_2,y_2]) == 0
Eq5 = Eq2 // (X-x_1) ; print("Eq5 = Eq2 // (X-x_1) = {}".format(Eq5))

#-X + l^2 - a - 2*x_1
x_4 = -Eq5.coefficient({X:0})/Eq5.coefficient({X:1}); print("x_4 = {}".format(x_4))

#l^2 - a - 2*x_1

#y coordinate of the point
y_4 = QQx(Lyl([x_4,Y])); print("knowing x_4, gets y0_4 with L(x_4,y0_4) = 0\ny0_4 = {}".format(y_4))
y_4 = -y_4; print("finally, y_4 = -y0_4 = {}".format(y_4))
