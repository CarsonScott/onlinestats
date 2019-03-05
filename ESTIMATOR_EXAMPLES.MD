# Estimator Examples

__Example #1__

In the first estimator example, we run a simple estimator 500 times with a constant observation of 3.

	from onlinestats import Estimator
	import matplotlib.pyplot as plt

	steps = 500
	observation = 3
	estimator = Estimator(learning_rate=0.1, decay_rate=0.1)

Here we have an estimator with a learning rate of 0.1, which dictates the rate of change of the delta value (i.e. the value added to the estimate at any given time) in the direction of the current error, and a decay rate of 0.1, which dictates the rate of change of the delta value in the direction of 0.
	
	estimates = []
	for i in range(steps):
		estimate = estimator.update(observation)
		estimates.append(estimate)

At each step we collect the current estimate given the current observation. Because we are using a constant observation, the estimate is expected to approach 3. 

	observations = [observation for i in range(steps)]
	plt.plot(observations, color='black')
	plt.plot(estimates, color='red')
  	plt.show()

We graph the estimates as well as the observations over time.

![Estimator Results 1](https://github.com/CarsonScott/onlinestats/blob/master/img/estimator_results_1.png)

As you can see the estimates eventually converge, more or less. The estimates oscillate around the observations because the estimator is constantly making adjustments. This allows it to change readily if the targets begin to change, as is the case in most real-world applications.

---

__Example #2__

In this example, we run a simple estimator 500 times with a constant observation of 3, just like in the first example.
	
	import matplotlib.pyplot as plt
	from onlinestats import Estimator

	steps = 500
	observation = 3
	estimator = Estimator(learning_rate=0.1, decay_rate=0.1, delta_limit=0.5)

Here we have an estimator with a learning rate of 0.1 and a decay rate of 0.1, as well as a delta limit of 0.5, which restricts the magnitude of the acceleration at any given time. 
	
	estimates = []
	for i in range(steps):
		estimate = estimator.update(observation)
		estimates.append(estimate)

At each step we collect the current estimate given the current observation. Because we are using a constant observation, the estimate is expected to approach 3. 

	observations = [observation for i in range(steps)]
	plt.plot(observations, color='black')
	plt.plot(estimates, color='red')
  	plt.show()

We graph the estimates as well as the observations over time. Since we used a constant observation in this example, the targets are represented by a straight line.

![Estimator Results 2](https://github.com/CarsonScott/onlinestats/blob/master/img/estimator_results_2.png)

As you can see the estimates eventually converge and do so without overcorrecting. The benefit of using a delta limit is that it keeps the rate of change from becoming too large at any given time. This can prevent overcorrections, or at least fix them quicker if they arise. Of course, there is a tradeoff as delta limits slow down the rate at which erroneous estimates are corrected. A comparison between the two examples is shown below.

![Estimator Results 1 and 2](https://github.com/CarsonScott/onlinestats/blob/master/img/estimator_results_1_and_2.png)
