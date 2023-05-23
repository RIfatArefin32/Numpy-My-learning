import numpy as np
import numpy.matlib

arr = np.matlib.empty((2,2))
print("\nThe empty matrix:\n",arr)

arr = np.matlib.rand((2,2))
print("The random matrix:\n", arr)

arr = np.matlib.zeros((2,2))
print(arr)

arr = np.matlib.ones((2,2))
print(arr)
print()

# numpy.matlib.eye(n, M,k, dtype): n = row; M = cols;
#  k = index of diagonal
arr = np.matlib.eye(3, 3, 0, dtype=float)
print("The Diagonal matrix is: \n", arr, "\n")
arr = np.matlib.eye(3, 4, 2, dtype=float)
print("The Diagonal matrix is: \n", arr, "\n")
print()

arr = numpy.matlib.identity(5, dtype=int)
print("The identity matrix is: \n", arr, "\n")

asArr = numpy.matlib.asarray(arr)
print(asArr)
print()

#Linear Algebra:
a = np.array([[1,2],[3,4]]) 
b = np.array([[11,12],[13,14]]) 
print(a)
print(b)
print("Dot product:\n", np.dot(a,b))
print("Dot product of two vectors: ", np.vdot(a,b))
print("Inner product of a and b: \n", np.inner(a,b))
print()
#For 1D array, inner product is same ase vector dot product
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Inner product of a and b: ", np.inner(a, b))
print()

#Matrix multiplication
a = [[1,0],[0,1]] 
b = [[4,1],[2,2]] 
print("Matrix multiplication is: \n", np.matmul(a,b))
a = np.arange(8).reshape(2,2,2) 
b = np.arange(4).reshape(2,2) 
print("Matrix multiplication is: \n", np.matmul(a,b))
print()


#Determinent of matrix
a = np.array([[1,2], [3,4]]) 
print("Determinent of A: ", np.linalg.det(a))
b = np.array([[6,1,1], [4, -2, 5], [2,8,7]]) 
print("Determinent of B: ", np.linalg.det(b))


#Inverse of a matrix
x = np.array([[1,2],[3,4]]) 
y = np.linalg.inv(x) 
print("The inverse matrix is: \n", y)
print(np.dot(x,y))


#matlib plot:
from matplotlib import pyplot as plt

'''
'-'     Solid line style


'--'    Dashed line style


'-.'    Dash-dot line style


':'     Dotted line style


'.'     Point marker


','     Pixel marker

'o'     Circle marker
	
'v'     Triangle_down marker

'^'     Triangle_up marker
	
'<'

Triangle_left marker


'>'

Triangle_right marker

	
'1'     Tri_down marker
'2'     Tri_up marker
'3'     Tri_left marker
'4'     Tri_right marker
's'     Square marker	
'p'     Pentagon marker	
'*'     Star marker
'h'     Hexagon1 marker	
'H'     Hexagon2 marker
'+'     Plus marker
'x'     X marker	
'D'     Diamond marker	
'd'     Thin_diamond marker	
'|'     Vline marker
'_'     Hline marker

'''




x = np.arange(1, 11)
y = 2*x + 5
plt.title("Straight line")
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.plot(x,y, 'P', 'y') 
plt.show()


'''
arr = np.arange(0, 91)
x = np.sin(10*arr*np.pi/180)
y = np.cos(10*arr*np.pi/180)
print(x)
print(y)

plt.subplot(2, 1, 1)
plt.title("Sine curve")
plt.xlabel("Angle in Degree")
plt.ylabel("Sine value")
plt.plot(arr, x)

plt.subplot(2, 1, 2)
plt.title("Cosine curve")
plt.xlabel("Angle in Degree")
plt.ylabel("Cosine value")
plt.plot(arr, y)

plt.show()
'''

'''
x = [5,8,10] 
y = [12,16,6]  

x2 = [6,9,11] 
y2 = [6,15,7] 
plt.bar(x, y, align = 'center') 
plt.bar(x2, y2, color = 'g', align = 'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  

plt.show()
'''