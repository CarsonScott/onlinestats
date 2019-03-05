# Estimator Example #1

In this example, we run a simple estimator 500 times with a constant observation of 3.

	steps = 500
	observation = 3
	estimator = Estimator(learning_rate=0.1, decay_rate=0.1)

Here we have an estimator with a learning rate of 0.1, which dictates the rate of change of acceleration and adjustment, and a decay rate of 0.1, which dictates the rate of change of acceleration. Specifically, the decay rate determines how quickly acceleration approaches 0, which is analogous to the friction applied to a moving body. Eventually the velocity of a moving body falls to zero if more friction is applied to it than acceleration.
	
	estimates = []
	for i in range(steps):
		estimate = estimator.update(observation)
		estimates.append(estimate)

At each step we collect the current estimate. Because at each point the estimator observes 3, the estimates at each point should converge to 3. 

	targets = [observation for i in range(steps)]
	plt.plot(targets, color='black')
	plt.plot(estimates, color='red')
  	plt.show()

We graph the estimates as well as the targets over time. Since we used a constant observation in this example, the targets are represented by a straight line.

Output:
![Estimator Results #1](https://github.com/CarsonScott/onlinestats/blob/master/img/estimator_results_1.png)

As you can see, the estimates and targets eventually converge, more or less. The estimates oscillate around the targets because the estimator is constantly making adjustments. This allows it to change readily if the targets begin to change, as is the case in most real-world applications.