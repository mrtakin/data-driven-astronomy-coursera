# Write your query function here
import numpy as np
def query(csv):
  data = np.loadtxt(csv, delimiter=',', usecols=(0, 2))
  return data[data[:, 1] > 1.0]


# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv')
  print(result)
