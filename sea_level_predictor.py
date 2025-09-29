import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    df_scatter = df.copy()
    x = df_scatter['Year']
    y = df_scatter['CSIRO Adjusted Sea Level']

    plt.scatter(x, y, color='blue')

    # Create first line of best fit
    res = linregress(x, y)

    x_low = 1880
    x_high = 2060
    x_extended = np.linspace(x_low, x_high, 100)

    plt.plot(x_extended, res.intercept + res.slope * x_extended, 'r', label='fitted line')

    # Create second line of best fit
    df_line = df.copy()
    df_line = df_line[df_line['Year'] >= 2000]
    x = df_line['Year']
    y = df_line['CSIRO Adjusted Sea Level']

    res = linregress(x, y)

    x_low = 2000
    x_extended = np.linspace(x_low, x_high, 100)

    plt.plot(x_extended, res.intercept + res.slope * x_extended, 'r', label='fitted line')
    plt.xlim([1880, 2060])
    plt.ylim([0, 12])

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


draw_plot()