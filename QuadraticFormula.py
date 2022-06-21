
#Quardratic Formula 
def Quardratic_Formula ():
    a = 1
    b = 2
    c = -15
    print ("a:",a)
    print ("b:",b)
    print ("c:",c)
    result = []
    x1 = (-b + (b*b - 4*a*c) ** (0.5) ) / (2*a)
    x2 = (-b - (b*b - 4*a*c) ** (0.5) ) / (2*a)
    result.append (x1)
    result.append (x2)
    print ("Result:", result)
    return

Quardratic_Formula()
