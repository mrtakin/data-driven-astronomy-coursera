# Write your load_fits function here.
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

def load_fits(file):
  hdu_list = fits.open(file)
  data = hdu_list[0].data
  return np.unravel_index(np.argmax(data), data.shape)


if __name__ == '__main__':
  # Run your `load_fits` function with examples:
  bright = load_fits('image2.fits')
  print(bright)

  # You can also confirm your result visually:
  from astropy.io import fits
  import matplotlib.pyplot as plt

  hdulist = fits.open('image2.fits')
  data = hdulist[0].data

  # Plot the 2D image data
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()

