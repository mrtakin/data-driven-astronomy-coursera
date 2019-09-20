# Write your mean_datasets function here
import numpy as np

def mean_datasets(csv_list):
  # Map csv list to np array list
  data_list = list(map(lambda csv: np.genfromtxt(csv,delimiter=',', dtype=float), csv_list))
  
  # Calculate element-wise mean and round it to 1-decimal place
  return np.around(np.mean(data_list, axis=0), decimals = 1)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example from the question:
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))

  # Run your function with the second example from the question:
  #print(mean_datasets(['data4.csv', 'data5.csv', 'data6.csv']))

