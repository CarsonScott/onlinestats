# Example #1

In the first model example, we run a simple model of 6 variables 1000 times on a set of 2 samples.

	from onlinestats import Estimator, Model
	import matplotlib.pyplot as plt

	steps = 1000
	variables = 6
	samples = [[1,0,1,0,1,0],
			   [0,1,0,1,1,0]]

	model=Model(variables,
		avg_estimator=Estimator(learning_rate=0.1, decay_rate=0.1, delta_limit=0.5),
		dev_estimator=Estimator(learning_rate=0.1, decay_rate=0.1, delta_limit=0.5, estimate_limit=(0,None)),
		cov_estimator=Estimator(learning_rate=0.1, decay_rate=0.1, delta_limit=0.5, estimate_limit=1))

Every estimator within the model shares an identical set of parameters with every other instance of that type. Here we define parameters for the average, standard-deviation, and covariance types of estimators in the model.
	
	covariance_matrix = None
	for i in range(int(steps / len(samples))):
		for observation in samples:
			covariance_matrix = model.update(observation)

We then update the model 1000 times by iterating through the set of samples. At each step, the model produces a covariance matrix based on the results of each estimator.

	plt.matshow(model.covariances, vmin=-1, vmax=1, cmap='hot')
	plt.colorbar()
	plt.show()

We graph the covariance matrix at the final time step. Given the samples we had previously defined, we should expect to see positive covariances between variables 0 and 2, as well as 1 and 3. We should expect to see mixed covariances between variable 4 and all other variables, as well as 5 and all other variables.

![Model Results 1](https://github.com/CarsonScott/onlinestats/blob/master/img/model_results_1.png)

As you can see, the covariances between pairs of variables are as expected.