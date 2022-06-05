import numpy as np 

mat = np.array([4,8,2])
print(mat)
print(type(mat))
print(mat.shape)
print(mat[1])
mat[1] = 20
print(mat)

mat2 = np.array([[5,8,7],[3,5,9]])
print(mat2)
print(type(mat2))
print(mat2.shape)
print(mat2[0][2])
mat2[0][0] = 1582
print(mat2)
print('----------------------------------')
print('\n')
mat3 = np.array([[[8,9,5,7],[6,8,4,4],[6,1,2,6]],[[8,2,5,1],[9,9,4,0],[2,2,1,2]],[[8,2,5,1],[9,9,4,0],[2,2,1,2]]],)
print(mat3)
print(mat3.shape)
mat3[1,2,2]=5000047
print(mat3)

mat4 = np.array([[1,2],[2,3]])
mat5 = np.array([[1,2],[2,3]])
mat6 = mat4 + mat5
print(mat4)
print(mat5)
print(mat6)