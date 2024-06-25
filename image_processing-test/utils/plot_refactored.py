
# plot.py

import matplotlib.pyplot as plt

def plot_data(data_list):
    """
    Plots the data using a line plot.

    Parameters:
    data_list (list of numeric): The data to be plotted.
    """
    plt.plot(data_list)
    plt.show()
