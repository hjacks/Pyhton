"""
This example uses the only the first feature
of the diabetes dataset, in order to illustrate
 a two-dimensional plot of this regression
 technique. The straight line can be seen in
 the plot, showing how linear regression
 attempts to draw a straight line that will
 best minimize the residual sum of squares
 between the observed responses in the dataset,
  and the responses predicted by the linear
  approximation.
"""

print(__doc__)

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()

diabetes_X = diabetes.data[:, np.newaxis, 2]
# print(diabetes)

diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)

diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)

# The mean squared error 均方误差
print("Mean squared error: %.2f"
      %mean_squared_error(diabetes_y_test
                          ,diabetes_y_pred))

# Explained variance score: 1 is perfect prediction
# 方差得分 1是完美预测
print("Variance score: %.2f" % r2_score(
    diabetes_y_test,diabetes_y_pred
))

plt.scatter(diabetes_X_test,diabetes_y_test, color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.savefig('LinearRegression.png')
plt.show()