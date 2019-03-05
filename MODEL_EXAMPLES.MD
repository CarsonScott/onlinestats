# Model Examples

__Example #1__

In the first model example, we run a simple model of 6 variables 1000 times on a set of 2 samples.

	from onlinestats import Estimator, Model
	import matplotlib.pyplot as plt

	steps = 1000
	variables = 6
	samples = [
		[1,0,1,0,1,0],
		[0,1,0,1,1,0]
	]

	model=Model(variables,
		avg_estimator=Estimator(learning_rate=0.1, decay_rate=0.1, delta_limit=0.5),
		dev_estimator=Estimator(learning_rate=0.1, decay_rate=0.1, delta_limit=0.5, estimate_limit=(0,None)),
		cor_estimator=Estimator(learning_rate=0.1, decay_rate=0.1, delta_limit=0.5, estimate_limit=1))

Every estimator within the model shares an identical set of parameters with every other instance of that type. Here we define parameters for the average, standard-deviation, and correlation types of estimators in the model.
	
	correlation_matrix = None
	for i in range(int(steps / len(samples))):
		for observation in samples:
			correlation_matrix = model.update(observation)

We then update the model 1000 times by iterating through the set of samples. At each step, the model produces a correlation matrix based on the results of each estimator.

	plt.matshow(model.correlations, vmin=-1, vmax=1, cmap='hot')
	plt.colorbar()
	plt.show()

We graph the correlation matrix at the final time step. Given the samples we had previously defined, we should expect to see high positive correlations between 0 and 2, and high positive correlations between 1 and 3. We should expect to see high negative correlations between 0 and 1, 0 and 3, 1 and 2, and 2 and 3. We should also expect low correlations between 4 and all other variables, as well as low correlations between 5 and all other variables.

![Model Results 1](https://github.com/CarsonScott/onlinestats/blob/master/img/model_results_1.png)

As you can see, the correlations between pairs of variables are as expected.
