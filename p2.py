#
# Using Numpy & Matplotlib: Given a 1-d array,
# ● Compute the number of occurrences of any subset array. For example:
# array = np.array([0, 1, 1, 1, 2, 2, 2, 1, 1, 3, 3, 3]) subset = np.array([1, 1])
# return: 3
# ● Plot a histogram of the unique values of the 1d-array

import numpy as np
import matplotlib.pyplot as plt

def subset_counter(array, subset):
    count = 0
    for i in range(array.shape[0]-subset.shape[0]):
        if (array[i:i+subset.shape[0]] == subset).all():
            count += 1
    return count


array = np.array([0, 1, 1, 1, 2, 2, 2, 1, 1, 3, 3, 3])
subset = np.array([1,1])

def histogram(array):
    for num in np.unique(array):
        count = np.where(array == num)[0].size
        plt.bar(num, count)
    plt.show()

count = subset_counter(array, subset)
histogram(array)