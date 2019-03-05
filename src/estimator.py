from .util import *

class Estimator:

	def __init__(self, learning_rate, decay_rate, delta_limit=None, estimate_limit=None):
		self.error=0
		self.delta=0
		self.estimate=0
		self.delta_min=None
		self.delta_max=None
		self.estimate_min=None
		self.estimate_max=None
		self.decay_rate=decay_rate
		self.learning_rate=learning_rate
		if iterable(delta_limit):
			self.delta_min=delta_limit[0]
			self.delta_max=delta_limit[1]
		elif delta_limit!=None:
			self.delta_min=-delta_limit
			self.delta_max=delta_limit
		if iterable(estimate_limit):
			self.estimate_min=estimate_limit[0]
			self.estimate_max=estimate_limit[1]
		elif estimate_limit!=None:
			self.estimate_min=-estimate_limit
			self.estimate_max=estimate_limit

	def compute_error(self, value):
		error=value-self.estimate
		return error

	def compute_delta(self, error):
		delta=self.delta+error*self.learning_rate
		delta=delta-self.delta/abs(self.delta)*self.decay_rate if self.delta!=0 else delta
		if self.delta_max!=None:
			if delta>self.delta_max:
				delta=self.delta_max
		if self.delta_min!=None:
			if delta<self.delta_min:
				delta=self.delta_min
		return delta

	def compute_estimate(self, delta):
		estimate=self.estimate + delta*self.learning_rate
		if self.estimate_max!=None:
			if estimate>self.estimate_max:
				estimate=self.estimate_max
		if self.estimate_min!=None:
			if estimate<self.estimate_min:
				estimate=self.estimate_min
		return estimate

	def update(self, value):
		self.error=self.compute_error(value)
		self.delta=self.compute_delta(self.error)
		self.estimate=self.compute_estimate(self.delta)
		return self.estimate