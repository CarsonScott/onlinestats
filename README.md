# OnlineStats

OnlineStats is a python library for creating statistical models in real-time from streaming data.

## Estimators

An estimator approximates the average value of a given variable over multiple time steps. At each step, the estimator calculates a new current estimate based on its current observation and its previous estimate.

The adjustment of an estimator at any given time is the difference in value between the next estimate and the current estimate. It determines how much the current estimate is changed between time t and t+1.

The acceleration of an estimator at any given time is the difference in value between the next adjustment and the current adjustment. It determines how much the current adjustment is changed between time t and t+1.

* Acceleration(t) ~ Observation(t) - Estimate(t-1)
* Adjustment(t) ~ Adjustment(t-1) + Acceleration(t)
* Estimate(t) ~ Estimate(t-1) + Adjustment(t)

[Estimator Examples](https://github.com/CarsonScott/onlinestats/blob/master/ESTIMATOR_EXAMPLES.MD)

***
## Statistical Models

A statistical model uses estimators to approximate the averages, standard distributions, and covariances of a set of variables over multiple time steps. At each step, the statistical model updates two estimators for each variable corresponding to its mean and standard deviation, and one estimator for each pair of variables corresponding to their covariance.

