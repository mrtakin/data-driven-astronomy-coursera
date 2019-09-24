# Write your query function here
# Write your query function here
import numpy as np
def query(star_csv, planet_csv):
  data_star = np.loadtxt(star_csv, delimiter=',', usecols=(0, 2))
  data_planet = np.loadtxt(planet_csv, delimiter=',', usecols=(0, 5))
  
  result = np.empty((0, 1), float)
  for star in data_star[data_star[:, 1] > 1, :]:
    its_planets = data_planet[data_planet[:, 0] == star[0], :]
    ratios = its_planets[:, [1]] / star[1] 
    
    result = np.append(result, ratios, axis=0)
  
  return np.sort(result, axis = 0)


# You can use this to test your code
# Everything inside this if-statement will be ignored by the automarker
if __name__ == '__main__':
  # Compare your function output to the SQL query
  result = query('stars.csv', 'planets.csv')
  
  print(result)
  
  
