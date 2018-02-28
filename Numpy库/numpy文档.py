import numpy as np
# numpy.apply_along_axis
def my_func(a):
    """Average first and last element of a 1-D array"""
    return (a[0]+a[-1])*0.5

b=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.apply_along_axis(my_func(),0,b)
