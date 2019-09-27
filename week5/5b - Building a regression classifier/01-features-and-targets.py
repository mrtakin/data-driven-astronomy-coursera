import numpy as np

def get_features_targets(data):
 
  colors = ['u', 'g', 'r', 'i', 'z']
  
  features = np.zeros((data.shape[0], 4))
  for i in range(len(colors) - 1):
    features[:, i] = data[colors[i]] - data[colors[i + 1]]
  
  targets = np.array(data['redshift'])
  
  return features, targets


if __name__ == "__main__":
  # load the data
  data = np.load('sdss_galaxy_colors.npy')
    
  # call our function 
  features, targets = get_features_targets(data)
    
  # print the shape of the returned arrays
  print(features[:2])
  print(targets[:2])

