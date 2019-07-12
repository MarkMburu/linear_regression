import numpy as np

class LinearRegression():
    
  alpha = 0.03
  iterations = 1500
  
  def __init__(self, X, y):
    
    self.n_samples = len(y)
    self.n_features = np.size(X,1)
    self.X = np.hstack((np.ones((self.n_samples,1)),(X-np.mean(X,0)) / np.std(X,0)))
    self.y = y[:, np.newaxis]
    self.params = np.zeros((self.n_features+1,1))
    
  def fit(self):

    for i in range(self.iterations):
       self.params = self.params - (self.alpha/self.n_samples) * \
       self.X.T @ (self.X @ self.params - self.y) 
    
    return self
     
  def score(self):
      
    y_pred = self.X @ self.params
    
    score = 1 - (((self.y - y_pred)**2).sum() / ((self.y-y.mean())**2).sum())
    
    return score

  def predict(self, X_test):
     y_test = np.hstack((np.ones((self.n_samples,1)),(X_test-np.mean(X_test,0)) \
                         / np.std(X_test,0))) @ self.params
     return y_test

