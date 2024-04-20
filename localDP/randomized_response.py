import numpy as np

class RandomizedResponse:
	def __init__(self, epsilon):
		self.p = 1 / (1 + np.exp(epsilon)) 

	def randomize_one_hot(self, data):
		return np.where(np.random.rand(*data.shape) < self.p, 1 - data, data)

	def randomize(self, data, datatype):
		if datatype=="one_hot":
			return self.randomize_one_hot(data)
		elif datatype=="boolean":
			return self.randomize_boolean(data)
		elif datatype=="integers":
			return self.randomize_integers(data)
		elif datatype=="rankings":
			return self.randomize_rankings(data)
		else:
			raise Exception("Unknown datatype!")
