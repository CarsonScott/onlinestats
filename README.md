# OnlineStats

OnlineStats is a python library for generating robust statistical models in real-time.

## Estimators

An estimator is used to approximate the average of a given variable in real-time. At each step, an estimator calculates an updated estimate value given its previous estimate and a current observation. Given a sufficient set of parameters, an estimator will settle on an estimate that describes its previous observations sufficiently well.

[Estimator Examples](https://github.com/CarsonScott/onlinestats/blob/master/ESTIMATOR_EXAMPLES.MD)

---

## Models

A statistical model is used to approximate the correlation coefficients between observable variables. At each step, a model calculates a revised correlation matrix by updating a set of estimators associated with each individual variable as well as each variable pair. Given a sufficient set of estimators, a model will converge on a correlation matrix that describes relationships between variables sufficiently well.

[Model Examples](https://github.com/CarsonScott/onlinestats/blob/master/MODEL_EXAMPLES.MD)
