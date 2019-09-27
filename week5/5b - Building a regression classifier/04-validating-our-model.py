import numpy as np
from sklearn.tree import DecisionTreeRegressor

# paste your get_features_targets function here
def get_features_targets(data):
 
  colors = ['u', 'g', 'r', 'i', 'z']
  
  features = np.zeros((data.shape[0], 4))
  for i in range(len(colors) - 1):
    features[:, i] = data[colors[i]] - data[colors[i + 1]]
  
  targets = np.array(data['redshift'])
  
  return features, targets

# paste your median_diff function here
def median_diff(predicted, actual):
  return np.median(np.abs(predicted - actual))


# write a function that splits the data into training and testing subsets
# trains the model and returns the prediction accuracy with median_diff
def validate_model(model, features, targets):
  # split the data into training and testing features and predictions
  split = features.shape[0] // 2
  train_features = features[:split]
  train_targets = targets[:split]
  
  test_features = features[split:]
  test_targets = targets[split:]

  # train the model
  dtr = DecisionTreeRegressor()
  dtr.fit(train_features, train_targets)

  # get the predicted_redshifts
  predictions = dtr.predict(test_features)
  
  # use median_diff function to calculate the accuracy
  return median_diff(test_targets, predictions)


if __name__ == "__main__":
  data = np.load('sdss_galaxy_colors.npy')
  features, targets = get_features_targets(data)

  # initialize model
  dtr = DecisionTreeRegressor()

  # validate the model and print the med_diff
  diff = validate_model(dtr, features, targets)
  print('Median difference: {:f}'.format(diff))

