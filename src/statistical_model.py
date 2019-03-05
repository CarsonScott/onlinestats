from .util import *

class StatisticalModel(Graph):

	def __init__(self, variables, mean_estimator, deviation_estimator, covariance_estimator):
		super().__init__()
		self.create_attribute('link', 'covariance_estimator')
		self.create_attribute('link', 'covariance')
		self.create_schema('variable', ['mean_estimator', 'deviation_estimator', 'mean', 'deviation'])

		if isinstance(variables, int):
			for i in range(variables):
				key=self.create_key('variable')
				self.create_object('variable', key, [copy(mean_estimator), copy(deviation_estimator), 0, 0])
		elif isinstance(variables, list):
			for key in variables:
				self.create_object('variable', key, [copy(mean_estimator), copy(deviation_estimator), 0, 0])
		for i in self.get_variables():
			for j in self.get_variables():
				self.create_link(i, j, [copy(covariance_estimator), 0])

	def get_variables(self):
		return self.get_instances('variable')

	def get_means(self):
		keys=self.get_variables()
		return [self[key, 'mean'] for key in keys]

	def get_deviations(self):
		keys=self.get_variables()
		return [self[key, 'deviation'] for key in keys]

	def get_covariances(self):
		keys=self.get_variables()
		return [[self.get_covariance(source, target) for target in keys] for source in keys]

	def get_mean_estimator(self, key):
		return self[key, 'mean_estimator']
	
	def get_deviation_estimator(self, key):
		return self[key, 'deviation_estimator']

	def get_covariance_estimator(self, source, target):
		return self[self.get_key(source, target), 'covariance_estimator']

	def get_mean(self, key):
		return self[key, 'mean']

	def get_deviation(self, key):
		return self[key, 'deviation']

	def get_covariance(self, source, target):
		return self[self.get_key(source, target), 'covariance']

	def set_mean_estimator(self, key, mean_estimator):
		self[key, 'mean_estimator']=mean_estimator

	def set_deviation_estimator(self, key, deviation_estimator):
		self[key, 'deviation_estimator']=deviation_estimator

	def set_covariance_estimator(self, source, target, covariance_estimator):
		self[self.get_key(source, target), 'deviation_estimator']=covariance_estimator

	def set_mean(self, key, mean):
		self[key, 'mean']=mean

	def set_deviation(self, key, deviation):
		self[key, 'deviation']=deviation

	def set_covariance(self, source, target, covariance):
		self[self.get_key(source, target), 'covariance']=covariance

	def update_mean(self, key):
		value=self.get_value(key)
		estimator=self.get_mean_estimator(key)
		mean=estimator.update(value)
		self.set_mean_estimator(key, estimator)
		self.set_mean(key, mean)

	def update_deviation(self, key):
		value=self.get_value(key)
		mean=self.get_mean(key)
		input=pow(value-mean, 2)
		estimator=self.get_deviation_estimator(key)
		estimate=estimator.update(input)
		deviation=math.sqrt(estimate) if estimate>0 else estimate
		self.set_deviation_estimator(key, estimator)
		self.set_deviation(key, deviation)

	def update_covariance(self, source, target):
		source_value=self.get_value(source)
		target_value=self.get_value(target)
		source_mean=self.get_mean(source)
		target_mean=self.get_mean(target)
		source_deviation=self.get_deviation(source)
		target_deviation=self.get_deviation(target)
		input=(source_value-source_mean)*(target_value-target_mean)
		input=input/(source_deviation*target_deviation) if source_deviation*target_deviation!=0 else input
		estimator=self.get_covariance_estimator(source, target)
		covariance=estimator.update(input)
		self.set_covariance_estimator(source, target, estimator)
		self.set_covariance(source, target, covariance)

	def update(self, values):
		keys=self.get_variables()
		for i in range(len(keys)):
			key=keys[i]
			value=values[i]
			self.set_value(key, value)
			self.update_mean(key)
			self.update_deviation(key)
		for source in keys:
			for target in keys:
				self.update_covariance(source, target)
