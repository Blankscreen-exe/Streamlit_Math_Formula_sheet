# EULERS METHOD
#  Yn+1 = Yn + h * f(x,y)

# function f(x , y) = x + y

def f(x , y):
    return x + y 

def euler():
    x = float(input("Enter value of x (x < y)"))
    y = float(input("Enter value of y (y > x) "))
    b = float(input("Enter value of b (step size)"))
    n = 5
    h = (b - x)/n

    arrX = [x]
    arrY = [y]

    while arrX[len(arrX) - 1] < b:
        arrX.append(arrX[len(arrX) - 1] + h)

    for i in range(len(arrX) - 1):
        arrY.append(arrY[len(arrY) - 1] + (h * f(arrX[i] , arrY[i])))
    print(arrY)

euler()    