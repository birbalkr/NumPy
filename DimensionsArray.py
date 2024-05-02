# ************* Dimensions of Array *************
import numpy as np
# 1-Dimensions Array
l=np.array([1,2,3,4])
print(l)
print(l.ndim) #Cheek Dimensions of array .ndim

# 2-Dimensions Array
print("\n")
l=np.array([[1,2,3,4],[4,5,7,8]])
print(l)
print(l.ndim) #Cheek Dimensions of array .ndim

# 3-Dimensions Array
print("\n")
l=np.array([[[1,2,3,4],[4,5,7,8],[8,9,6,4]]])
print(l)
print(l.ndim) #Cheek Dimensions of array .ndim
