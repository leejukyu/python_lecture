def root_ex(a,b,c):
    x_1 = (-b + (b**2-4*a*c)**0.5)/(2*a)
    x_2 = (-b - (b**2-4*a*c)**0.5)/(2*a)
    print(x_1,x_2)
    return x_1, x_2
root_ex(2,-1,-6)