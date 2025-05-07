import numpy as np

#Standardization
def standardization(np_array):

    size = np.size(np_array)

    if size == 0:
        print("array is empty")
        return np_array

    array_mean = np.sum(np_array) / size
    array_std = np.sqrt(np.sum(np.power(np_array - array_mean, 2)) / size)
    new_np_array = (np_array - array_mean) / array_std
    return new_np_array

rng = np.random.default_rng(42)
arr = np.arange(0, 11, 2) 
print(standardization(arr))