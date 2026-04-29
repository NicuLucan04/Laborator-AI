import numpy as np
# a= np.array([1,2,3])
# print(a)
# print(type(a))
# print(a.dtype)
# print(a.shape)
# print(a[0])
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b.shape)     
# print(b[0][2])    
# print(b[0, 2])     

# c = np.asarray([[1, 2], [3, 4]])
# print(type(c))     
# print(c.shape)     



# zero_array = np.zeros((3, 2)) 
# print(zero_array)


# ones_array = np.ones((2, 2)) 
# print(ones_array)


# constant_array = np.full((2, 2), 8) 
# print(constant_array)


# identity_matrix = np.eye(3) 
# print(identity_matrix)

# ############################

# first_5 = np.arange(5)
# print(first_5)

# array_to_slice = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
# slice = array_to_slice[:, 0:3]
# print(slice)

# print(array_to_slice[0][0])
# slice[0][0] = 100
# print(array_to_slice[0][0])

# slice_copy = np.copy(array_to_slice[:, 0:3])
# slice_copy[0][0] = 100
# print(slice_copy[0][0])
# print(array_to_slice[0][0])

# # Functii matematice

# x = np.array([[1,2],[3,4]], dtype=np.float64)
# y = np.array([[5,6],[7,8]], dtype=np.float64)

# print(x + y)
# print(np.add(x, y))

# print(x - y)
# print(np.subtract(x, y))

# print(x * y)
# print(np.multiply(x, y))

# print(x / y)
# print(np.divide(x, y))

# print(np.sqrt(x))

# my_array = np.arange(5)
# powered = np.power(my_array, 3)
# print(powered)





# x = np.array([[1, 2],[3, 4]])
# y = np.array([[5, 6],[7, 8]])
# v = np.array([9, 10])
# w = np.array([11, 12])

# print(v.dot(w))
# print(np.dot(v, w))

# print(np.matmul(x, v))

# print(np.matmul(x, y))

# # operatii pe matrici

# my_array = np.array([[1, 2, 3], [4, 5, 6]])
# print(my_array.T)

# my_array = np.array([[1., 2.], [3., 4.]])
# print(np.linalg.inv(my_array))

# # functii care realizeaza operatii pe o anumita dimensiune

# x = np.array([[1, 2],[3, 4]])

# print(np.sum(x))
# print(np.sum(x, axis=0))
# print(np.sum(x, axis=1))
# print(np.sum(x, axis=(0, 1)))
import matplotlib.pyplot as plt
# x = np.arange(0, 3 * np.pi, 0.1)
# y = np.sin(x)

# plt.plot(x, y)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Sine')
# plt.legend(['Sine'])
# plt.show()
x = np.arange(0, 3 * np.pi, 0.1)
y_1 = np.sin(x)
y_2 = np.cos(x)

plt.plot(x, y_1)
plt.plot(x, y_2)

plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()
