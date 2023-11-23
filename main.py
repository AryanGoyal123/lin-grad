"""
This is some of the initial code for basic derivative functions
"""
import numpy as np
import matplotlib.pyplot as plt


def derivative(func, x):
    """
    Basic method to take a derivative of a function
    input: function, x
    output: slope
    """
    yi = func(x)
    h = 0.0001
    yf = func(x + h)

    dy = ((yf - yi) / h)
    return dy


def xfunc(x=0):
    a = 2
    b = 5
    c = 3
    # quadratic equation
    return a * x ** 2 + b * x + c


x = np.arange(-5, 5, 0.1)
y = xfunc(x)
ans = derivative(xfunc, x)

plt.plot(x, y)
plt.plot(x, ans)
plt.grid(True)
plt.show()
