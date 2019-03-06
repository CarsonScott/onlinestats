from .util import *

class Correlator:

	def __init__(self, variables, avg_estimator, dev_estimator, cor_estimator):
		self.values=[]
		self.averages=[]
		self.deviations=[]
		self.correlations=[]
		self.avg_estimators=[]
		self.dev_estimators=[]
		self.cor_estimators=[]
		for i in range(variables):
			self.values.append(0)
			self.averages.append(0)
			self.deviations.append(0)
			self.correlations.append([])
			self.avg_estimators.append(copy(avg_estimator))
			self.dev_estimators.append(copy(dev_estimator))
			self.cor_estimators.append([])
			for j in range(variables):
				self.correlations[i].append(0)
				if j>=i:
					self.cor_estimators[i].append(copy(cor_estimator))
				else:self.cor_estimators[i].append(None)

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

	def update_correlation(self, index1, index2):
		value1=self.values[index1]
		value2=self.values[index2]
		average1=self.averages[index1]
		average2=self.averages[index2]
		deviation1=self.deviations[index1]
		deviation2=self.deviations[index2]
		numerator=(value1-average1)*(value2-average2)
		denominator=deviation1*deviation2
		x=numerator/denominator if denominator!=0 else numerator
		estimator=self.cor_estimators[index1][index2]
		correlation=estimator.update(x)
		self.correlations[index1][index2]=correlation
		self.correlations[index2][index1]=correlation

	def update(self, values):
		self.values=values
		for i in range(len(self.values)):
			self.update_average(i)
			self.update_deviation(i)
		for i in range(len(self.values)):
			for j in range(i, len(self.values)):
				self.update_correlation(i,j)
		return self.correlations