# Model Examples

__Example #1__

In the first example, we run a simple correlator of 6 variables 1000 times on a set of 2 samples.

	from onlinestats import Estimator, Model
	import matplotlib.pyplot as plt

	steps = 1000
	variables = 6
	samples = [
		[1,0,1,0,1,0],
		[0,1,0,1,1,0]
	]

	correlator=Correlator(variables,
		avg_estimator=Estimator(learning_rate=0.1, decay_rate=0.1, delta_limit=0.5),
		dev_estimator=Estimator(learning_rate=0.1, decay_rate=0.1, delta_limit=0.5, estimate_limit=(0,None)),
		cor_estimator=Estimator(learning_rate=0.1, decay_rate=0.1, delta_limit=0.5, estimate_limit=1))

Every estimator within the correlator shares an identical set of parameters with every other instance of that type. Here we define parameters for the average, standard-deviation, and correlation types of estimators in the correlator.
	
	correlation_matrix = None
	for i in range(int(steps / len(samples))):
		for observation in samples:
			correlation_matrix = correlator.update(observation)

We then update the correlator 1000 times by iterating through the set of samples. At each step, the correlator produces a correlation matrix based on the results of each estimator.

	plt.matshow(correlation_matrix, vmin=-1, vmax=1, cmap='hot')
	plt.colorbar()
	plt.show()

We graph the correlation matrix at the final time step. Given the samples we had previously defined, we should expect to see high positive correlations between 0 and 2, and high positive correlations between 1 and 3. We should expect to see high negative correlations between 0 and 1, 0 and 3, 1 and 2, and 2 and 3. We should also expect low correlations between 4 and all other variables, as well as low correlations between 5 and all other variables.

![Model Results 1](https://github.com/CarsonScott/onlinestats/blob/master/img/model_results_1.png)

As you can see, the correlations between pairs of variables are as expected.

---

__Example #2__

In this example, we run a simple cross-correlator of 3 variables 300 times on a set of 3 samples, with a delay constant of 1.
	
	from onlinestats import Estimator, Model
	import matplotlib.pyplot as plt
	
	steps = 500
	delay = 1
	variables = 3
	samples = [
		[1,0,0],
		[0,1,1],
		[0,0,1]]

	cross_correlator = CrossCorrelator(variables, delay,
		avg_estimator=Estimator(learning_rate=0.1, decay_rate=0.1),
		dev_estimator=Estimator(learning_rate=0.1, decay_rate=0.1),
		cor_estimator=Estimator(learning_rate=0.1, decay_rate=0.1))

	index = 0
	for i in range(int(steps / len(samples))):
		sample = samples[index]
		index = index+1 if index+1 < len(samples) else 0
		correlation_matrix = cross_correlator.update(sample)

	plt.matshow(correlation_matrix, vmin=-1, vmax=1, cmap='hot')
	plt.colorbar()
	plt.show()
	
We graph the correlation matrix at the final time step. Unlike the correlation matrix produced by a correlator, cross-correlators are order-dependent. This means that the correlation between 0 and 1 is different than that of 1 and 0. With that in mind, we should expect to see positive correlations between 0 and 1, 0 and 2, 1 and 2, 2 and 2, and 2 and 0. All the rest are expected to be negative.

![Model Results 2](https://github.com/CarsonScott/onlinestats/blob/master/img/model_results_2.png)

As you can see, the results are as expected.
