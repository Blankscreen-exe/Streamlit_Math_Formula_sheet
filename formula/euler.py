# EULERS METHOD
#  Yn+1 = Yn + h * f(x,y)

# function f(x , y) = x + y

def f(x , y):
    return x + y 

def euler(x,y,b):

    n = 5
    h = (b - x)/n

    arrX = [x]
    arrY = [y]

    while arrX[len(arrX) - 1] < b:
        arrX.append(arrX[len(arrX) - 1] + h)

    for i in range(len(arrX) - 1):
        arrY.append(arrY[len(arrY) - 1] + (h * f(arrX[i] , arrY[i])))
    return arrY

