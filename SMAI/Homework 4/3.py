import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plot(a_mean, b_mean, a_covar, b_covar):
	# print(a_mean)
	# print(a_covar)
	A = np.random.multivariate_normal(a_mean, a_covar, 1000).T
	B = np.random.multivariate_normal(b_mean, b_covar, 1000).T

	fig = plt.figure()
	ax = fig.add_subplot(221, projection='3d')
	ax.set_title("3D")
	ax.scatter(A[0,:], A[1,:], A[2,:], color='g', marker='o')
	ax.scatter(B[0,:], B[1,:], B[2,:], color='b', marker='x')

	plt.subplot(2,2,2)
	plt.title("X-Y")
	plt.scatter( A[0,:] , A[1,:] , color='g', marker='o')
	plt.scatter( B[0,:] , B[1,:] , color='b', marker='x')

	plt.subplot(2,2,3)
	plt.title("Y-Z")
	plt.scatter( A[1,:] , A[2,:] , color='g', marker='o')
	plt.scatter( B[1,:] , B[2,:] , color='b', marker='x')

	plt.subplot(2,2,4)
	plt.title("Z-X")
	plt.scatter( A[2,:] , A[0,:] , color='g', marker='o')
	plt.scatter( B[2,:] , B[0,:] , color='b', marker='x')
	plt.show()


a_mean = [random.random()*10, random.random()*10, random.random()*10]
a_covar = [[random.random() * 10, 0, 0],
			[0, random.random() * 10, 0],
			[0, 0, random.random() * 10]]
b_mean = [random.random()*10, random.random()*10, random.random()*10]
b_covar = [[random.random() * 10, 0, 0],
			[0, random.random() * 10, 0],
			[0, 0, random.random() * 10]]

plot(a_mean, b_mean, a_covar, b_covar)

a_covar = [[1, 1, 1],
			[1, 4, 1],
			[1, 1, 9]]
b_covar = [[1, 2, 0],
			[2, 4, 0],
			[0, 0, 3]]
plot(a_mean, b_mean, a_covar, b_covar)
b_mean = a_mean
plot(a_mean, b_mean, a_covar, b_covar)