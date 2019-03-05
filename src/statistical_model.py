from .util import *

class StatisticalModel:

	def __init__(self, variables, avg_estimator, dev_estimator, cov_estimator):
		self.values=[]
		self.averages=[]
		self.deviations=[]
		self.covariances=[]
		self.avg_estimators=[]
		self.dev_estimators=[]
		self.cov_estimators=[]
		for i in range(variables):
			self.values.append(0)
			self.averages.append(0)
			self.deviations.append(0)
			self.covariances.append([])
			self.avg_estimators.append(copy(avg_estimator))
			self.dev_estimators.append(copy(dev_estimator))
			self.cov_estimators.append([])
			for j in range(variables):
				self.covariances[i].append(0)
				if j>=i:
					self.cov_estimators[i].append(copy(cov_estimator))
				else:self.cov_estimators[i].append(None)

	def update_value(self, index, value):
		self.values[index]=value

	def update_average(self, index):
		value=self.values[index]
		estimator=self.avg_estimators[index]
		average=estimator.update(value)
		self.averages[index]=average

	def update_deviation(self, index):
		value=self.values[index]
		average=self.averages[index]
		x=pow(value-average, 2)
		estimator=self.dev_estimators[index]
		deviation=estimator.update(x)
		deviation=math.sqrt(deviation) if deviation > 0 else 0
		self.deviations[index]=deviation

	def update_covariance(self, index1, index2):
		value1=self.values[index1]
		value2=self.values[index2]
		average1=self.averages[index1]
		average2=self.averages[index2]
		deviation1=self.deviations[index1]
		deviation2=self.deviations[index2]
		numerator=(value1-average1)*(value2-average2)
		denominator=deviation1*deviation2
		x=numerator/denominator if denominator!=0 else numerator
		estimator=self.cov_estimators[index1][index2]
		covariance=estimator.update(x)
		self.covariances[index1][index2]=covariance
		self.covariances[index2][index1]=covariance

	def update(self, values):
		self.values=values
		for i in range(len(self.values)):
			self.update_average(i)
			self.update_deviation(i)
		for i in range(len(self.values)):
			for j in range(i, len(self.values)):
				self.update_covariance(i,j)
