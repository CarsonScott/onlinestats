# OnlineStats

OnlineStats is a python library for generating robust statitistical models in real-time. Using a hierarchy of online approximation functions, OnlineStats creates covariance matrices 

## Estimators

An estimator is used to approximate the average of a given variable in real-time. At each step, an estimator calculates an updated estimate value given its previous estimate and a current observation. Given a sufficient set of parameters, an estimator will settle on an estimate that describes its previous observations sufficiently well.

[Estimator Examples](https://github.com/CarsonScott/onlinestats/blob/master/ESTIMATOR_EXAMPLES.MD)

---

## Models

A model uses estimators to approximate a correlation matrix given a set of variables. At each step, a model updates a set of estimators that together predict the correlation coefficient for each pair of variables. There are two types of models, namely correlators and cross-correlators. A cross-correlator does the same as a correlator, that is produces a correlation matrix, however the correlation coefficients are calculated at each time step between a set of variables at the current time and the same set of variables at some previous time delayed by a constant factor.

[Model Examples](https://github.com/CarsonScott/onlinestats/blob/master/MODEL_EXAMPLES.MD)
