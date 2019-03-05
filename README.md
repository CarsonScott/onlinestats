# OnlineStats

OnlineStats is a python library for generating robust statistical models in real-time.

## Estimators

An estimator is used to approximate the average of a given variable in real-time. At each step, an estimator calculates an updated estimate value given its previous estimate and a current observation. Given a sufficient set of parameters, an estimator will settle on an estimate that describes its previous observations sufficiently well.

[Estimator Examples](https://github.com/CarsonScott/onlinestats/blob/master/ESTIMATOR_EXAMPLES.MD)

---

## Models

A model is used to approximate the correlation coefficients between a set of variables. At each step, a statistical model updates the average and standard-deviation estimators for each variable, as well as the correlation estimator for each pair of variables. The result is a correlation matrix that iteratively improves to better fit the stream of observations.

[Model Examples](https://github.com/CarsonScott/onlinestats/blob/master/MODEL_EXAMPLES.MD)
