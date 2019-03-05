# OnlineStats

Onlinestats is a python library for creating statistical models of streaming data.

## Estimators

An estimator approximates the average value of a given variable over multiple time steps. At each step, the estimator calculates a new current estimate based on its current observation and its previous estimate.

The adjustment of an estimator at any given time is the difference in value between the next estimate and the current estimate. It determines how much the current estimate is changed between time t and t+1.

The acceleration of an estimator at any given time is the difference in value between the next adjustment and the current adjustment. It determines how much the current adjustment is changed between time t and t+1.

* Acceleration(t) ~ Observation(t) - Estimate(t-1)
* Adjustment(t) ~ Adjustment(t-1) + Acceleration(t)
* Estimate(t) ~ Estimate(t-1) + Adjustment(t)

***

__Example #1__

In this example, we run a simple estimator 500 times with a constant observation.

	estimator = Estimator(learning_rate=0.1, decay_rate=0.1)

Here we have an estimator with a learning rate of 0.1, which dictates the rate of change of acceleration and adjustment, and a decay rate of 0.1, which dictates the rate of change of acceleration. Specifically, the decay rate determines how quickly acceleration approaches 0, which is analogous to the friction applied to a moving body. Eventually the velocity of a moving body falls to zero if more friction is applied to it than acceleration.

	observation = 3

We have a constant observation of 3, which means that at each point in time the estimator recieves a value of 3 as its observation, and thus should adjust its estimate to be as close to 3 as possible.

	steps = 500

The number of steps in this example is 500, meaning the estimator will receive 500 observations in total.
	
	estimates = []
	for i in range(steps):
		estimate = estimator.update(observation)
		estimates.append(estimate)

At each step we collect the current estimate. We may now graph the results.

	targets = [target for i in range(steps)]
	plt.plot(targets, color='black')
	plt.plot(estimates, color='red')
  plt.show()
