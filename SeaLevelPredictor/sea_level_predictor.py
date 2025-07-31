import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("/Users/nikhilsethu1/Coding/Code/DAPythonFCC/SeaLevelPredictor/epa-sea-level.csv")
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.7, s=30)
    
    # Create first line of best fit (using all data)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create x values from first year to 2050 for the first line
    years_extended = np.arange(df['Year'].min(), 2051)
    line1_y = slope1 * years_extended + intercept1
    ax.plot(years_extended, line1_y, 'r-', linewidth=2, label='Best fit line (all data)')
    
    # Create second line of best fit (using data from 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create x values from 2000 to 2050 for the second line
    years_2000_2050 = np.arange(2000, 2051)
    line2_y = slope2 * years_2000_2050 + intercept2
    ax.plot(years_2000_2050, line2_y, 'g-', linewidth=2, label='Best fit line (2000-present)')
    
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()