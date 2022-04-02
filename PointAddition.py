
#Adding two point P,Q on the elliptic curve
#We define a polynomial ring
QQx.<a,b,l,x_1,y_1,x_2,y_2> = QQ[]
QQE.<X,Y> = QQx[]

#We define the line passing through 2 points on the curve, l for the slope of line
L = Y - (l*(X-x_1) + y_1)
Ly = -L.coefficient({Y:0})/L.coefficient({Y:1})

#We define our elliptic curve
E = Y^2 - X^3 - a*X^2 - X

#The curve and the line intersect in a set of points
#and when we evaluate the curve for the y values satisfying the line
#we obtain an equation in x whose solution is the intersection of the line and the curve

Eq = E([X, Ly]); print("E(X, value of Y in the line L) = {}".format(Eq))
#-X^3 + (l^2 - a)*X^2 + (-2*l^2*x_1 + 2*l*y_1 - 1)*X + l^2*x_1^2 - 2*l*x_1*y_1 + y_1^2

print("L intersects E has solutions Eq, and\nEq mod (X-x_1) = {} = {} mod E([x_1,y_1])".format(Eq % (X-x_1), (Eq % (X-x_1)) % E([x_1,y_1])))
assert (Eq % (X-x_1)) % E([x_1,y_1]) == 0
print("simplify Eq by X-x1")
#-a*x_1^2 - x_1^3 + y_1^2 - x_1 

#We divide the curve by the roots we already know to simplify the curve
Eq2 = Eq // (X-x_1) ; print("Eq2 = Eq // (X-x_1) = {}".format(Eq2))
#-X^2 + (l^2 - a - x_1)*X - l^2*x_1 - a*x_1 - x_1^2 + 2*l*y_1 - 1

Eq3 = Eq2 % (X-x_2); print("Eq3 = Eq2 % (X-x_2) = {}".format(Eq3))
#-l^2*x_1 + l^2*x_2 - a*x_1 - x_1^2 + 2*l*y_1 - a*x_2 - x_1*x_2 - x_2^2 - 1


#We substitute the slope for l
Eq3 = QQx(Eq3)
lambda_add = (y_2-y_1)/(x_2-x_1)
Eq4 = Eq3([a,b,lambda_add,x_1,y_1,x_2,y_2]); print("Eq4 = Eq3(l = {})".format(lambda_add))
N = Eq4.numerator(); print("N = Eq4.numerator() = {} = {} mod (E(x_1,y_1), E(x_2,y_2))".format(N, N % (E(x_1,y_1)) % E(x_2,y_2)))
#a*x_1^2 + x_1^3 - a*x_2^2 - x_2^3 - y_1^2 + y_2^2 + x_1 - x_2 

D = Eq4.denominator();  print("N = Eq4.denominator() = {}".format(D))
#-x_1 + x_2
assert (N % (E(x_1,y_1))) % E(x_2,y_2) == 0

print("Simplify Eq by (X-x2) because Eq % (X-x2) = 0 mod the curve equation, when replacing l by its value")
Eq5 = Eq2 // (X-x_2); print("Eq5 = Eq2 // (X-x_2) = {}".format(Eq5))
print("The equation is now linear in X, that is a solution x_3 for X can be deduced easily")
x_3 = -Eq5.coefficient({X:0})/Eq5.coefficient({X:1}); print("x_3 = {}".format(x_3))

#y coordinate of the point 
y_3 = QQx(Ly([x_3,Y])); print("knowing x_3, gets y0_3 with L(x_3,y0_3) = 0\ny0_3 = {}".format(y_3))
y_3 = -y_3; print("finally, y_3 = -y0_3 = {}".format(y_3))