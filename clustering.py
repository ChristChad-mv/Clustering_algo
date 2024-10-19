import numpy as np
from math import sqrt

"""
@param : numbers_point -> This param allow user to set the number of point at the start
This function allow the collection of points
And store the data inside of dictionary
"""
def data_collection(numbers_points):
  coordinates = []
  for i in range(numbers_points):
    x = float(input(f"Enter the abscis of point {i+1} : "))
    y = float(input(f"Enter the ordinate of point {i+1} : "))
    coordinates.append({"x" : x, "y": y})
  return coordinates

