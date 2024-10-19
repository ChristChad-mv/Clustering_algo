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

"""
Extraction of data
For more efficient manipulation of points, we have to extract the points got from the user and store if differently
@param : data -> It's our data, the database

This function return our data separatly in two lists. 
We prepare the data for Z-normalization
"""

def extract_data(data):
    coord_x_list = []
    coord_y_list = []

    for point in data: 
        coord_x_list.append(point["x"])
        coord_y_list.append(point["y"])
    return coord_x_list, coord_y_list
