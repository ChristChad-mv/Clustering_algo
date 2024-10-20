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

"""
@ Params
1. numbers of centroids -> It's for the initial centroids entered by the user
2. coord_x_norm and coord_y_norm are the coordinates x and y normalized by the function data_normalizaion
3. coordinate_x, coordinate_y are t


# Output -> We want here to have the centroids normalized and non-normalized

"""

def having_centroids(number_of_centroids, coord_x_norm, coord_y_norm, coordinates_x, coordinates_y):
  centroids_norm = []
  centroids = []

  for i in range(1, number_of_centroids + 1):
    while True: 
      centroide = input(f"Enter the centroid {i} (e.g A1, A3, A8) :")

      # The number of centroids enter by the user must be less than the total number of all points entered
      # We get just the second element because if the user enter A1 we just want to have the 1

      index = int(centroide[1:])

      if index > len(coord_x_norm):
        print(f"Invalid number ! You can only use the centroids in range from 1 to the number of points entered at the start")
      else :
        centroids_norm.append({"x": coord_x_norm[index - 1], "y": coord_y_norm[index - 1]})
        centroids.append({ "x": coordinates_x[index - 1], "y": coordinates_y[index - 1] })
        # We use index - 1 because we want to have the correct coordinates of the points.
        # If the user enter 1 but we'll start the count by 0
        break
    return centroids, centroids_norm

  
"""
@ Params x1, x2, y1, y2 are the coordinates
And the function will return the eucliedian distance between these points
"""
def calculate_euclidean_distance(x1, y1, x2, y2):
  return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)