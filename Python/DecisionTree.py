import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
import numpy as np

np.random.seed(0)

X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y += 0.1 * (np.random.rand(80) - 0.5)

X_train, X_test = X[:60], X[60:]
y_train, y_test = y[:60], y[60:]

regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

plt.figure()
plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_test, y_pred, color="cornflowerblue", linewidth=2, label="prediction")
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()