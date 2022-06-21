def Quadratic(a,b,c):
    result = []
    x1 = (-b + (b*b - 4*a*c) ** (0.5) ) / (2*a)
    x2 = (-b - (b*b - 4*a*c) ** (0.5) ) / (2*a)
    result.append(x1)
    result.append(x2)
    return result
