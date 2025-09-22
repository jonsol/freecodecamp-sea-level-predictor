import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    anos = range(df['Year'].min(), 2051)
    plt.plot(anos, [intercept + slope*x for x in anos], 'r', label='Ajuste total')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    anos_2000 = range(2000, 2051)
    plt.plot(anos_2000, [intercept2 + slope2*x for x in anos_2000], 'g', label='Ajuste desde 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__ == "__main__":
    draw_plot()
    plt.show()