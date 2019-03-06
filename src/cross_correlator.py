from .util import *
from .correlator import Correlator

class CrossCorrelator(Correlator):
	
	def __init__(self, variables, memory, avg_estimator, dev_estimator, cor_estimator):
		super().__init__(variables, avg_estimator, dev_estimator, cor_estimator)
		self.memories=[[0 for i in range(memory)] for j in range(variables)]
		for i in range(len(self.cor_estimators)):
			for j in range(len(self.cor_estimators[i])):
				if self.cor_estimators[i][j]==None:
					self.cor_estimators[i][j]=copy(cor_estimator)

	def update_memory(self, index):
		value=self.values[index]
		self.memories[index].append(value)
		del self.memories[index][0]

	def update_correlation(self, index1, index2):
		memories=self.memories[index1]
		total=0
		for i in range(len(memories)):
			value1=memories[i]
			value2=self.values[index2]
			average1=self.averages[index1]
			average2=self.averages[index2]
			deviation1=self.deviations[index1]
			deviation2=self.deviations[index2]
			numerator=(value1-average1)*(value2-average2)
			denominator=deviation1*deviation2
			data=numerator/denominator if denominator!=0 else numerator
			total+=data/(len(memories)-i+1)
		estimator=self.cor_estimators[index1][index2]
		correlation=estimator.update(total)
		self.correlations[index1][index2]=correlation
	def update(self, values):
		for i in range(len(self.values)):
			self.update_memory(i)
			self.values[i]=values[i]
			self.update_average(i)
			self.update_deviation(i)
		for i in range(len(self.values)):
			for j in range(len(self.values)):
				self.update_correlation(i,j)
		return self.correlations
