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

"""
@params : list_coord_x and list_coord_y
We get the data in separate list from the function extract data and now, we can do some preprocessing
We prepare our data because we want to avoid the scale effects in our calculus.
"""

def data_normalization(list_coord_x, list_coord_y):
    # We transform the list to a array numpy because we have more flexibity when we work with numpy. We have more function ready to help us
    list_coord_x_array = np.array(list_coord_x)
    list_coord_y_array = np.array(list_coord_y)

    # With the formula of normalization 
    liste_coord_x_normalized = (list_coord_x_array - np.mean(list_coord_x_array)) / np.std(list_coord_x_array)
    liste_coord_y_normalized = (list_coord_y_array - np.mean(list_coord_y_array)) / np.std(list_coord_y_array)

    return liste_coord_x_normalized, liste_coord_y_normalized
