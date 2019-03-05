# OnlineStats

OnlineStats is a python library for creating statistical models in real-time from streaming data.

## Estimators

An estimator is used to approximate the average of a given variable in real-time. At each step, an estimator calculates an updated estimate value given its previous estimate and a current observation. Given a sufficient set of parameters, an estimator will settle on an estimate that describes its previous observations sufficiently well.

[Estimator Examples](https://github.com/CarsonScott/onlinestats/blob/master/ESTIMATOR_EXAMPLES.MD)

***
## Statistical Models

A statistical model uses estimators to approximate the averages and standard distributions of a set of variables, as well as covariances between pairs of variables. At each step, a statistical model updates the average and standard deviation estimators for each variable, and then a covariance estimator for each pair, resulting in a covariance matrix.
