import numpy as np
from sklearn.tree import DecisionTreeRegressor

# copy in your get_features_targets function here
def get_features_targets(data):
 
  colors = ['u', 'g', 'r', 'i', 'z']
  
  features = np.zeros((data.shape[0], 4))
  for i in range(len(colors) - 1):
    features[:, i] = data[colors[i]] - data[colors[i + 1]]
  
  targets = np.array(data['redshift'])
  
  return features, targets

# load the data and generate the features and targets
data = np.load('sdss_galaxy_colors.npy')
features, targets = get_features_targets(data)
  
# initialize model
dtr = DecisionTreeRegressor()

# train the model
dtr.fit(features, targets)

# make predictions using the same features
predictions = dtr.predict(features)

# print out the first 4 predicted redshifts
print(predictions[:4])

