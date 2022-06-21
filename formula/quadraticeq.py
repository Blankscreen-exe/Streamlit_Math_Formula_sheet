import math  

def quadraticeq(a,b,c):
  
  # calculate the discriminant  
  d = (b**2) - (4*a*c)  
    
  # find two solutions  
  sol1 = (-b- (d)**(1/2))/(2*a)  
  sol2 = (-b+ (d)**(1/2))/(2*a)  
  return (sol1,sol2,) 
