# Write your mean_fits function here:
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def mean_fits(files):
  # Map csv list to np array list
  data_list = list(map(lambda file: fits.open(file)[0].data, files))
  
  # Calculate element-wise mean of stack images
  return np.mean(data_list, axis=0)


if __name__ == '__main__':
  
  # Test your function with examples from the question
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits', 'image3.fits', 'image4.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
