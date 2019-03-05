# OnlineStats

OnlineStats is a python library for creating statistical models in real-time from streaming data.

## Estimators

An estimator is used to approximate the average of a given variable in real-time. At each step, an estimator calculates an updated estimate value given its previous estimate and a current observation. Given a sufficient set of parameters, an estimator will settle on an estimate that describes its previous observations sufficiently well.

[Estimator Examples](https://github.com/CarsonScott/onlinestats/blob/master/ESTIMATOR_EXAMPLES.MD)

---

## Models

A model uses estimators to approximate the average and standard distribution of each variable in a set, as well as the covariance between every pair of variables. At each step, a statistical model updates the average and standard deviation estimators for each variable, and uses the resulting estimates to update a covariance estimator for each pair. The result is a covariance matrix that relates each variable with every other variable.

[Model Examples](https://github.com/CarsonScott/onlinestats/blob/master/MODEL_EXAMPLES.MD)
