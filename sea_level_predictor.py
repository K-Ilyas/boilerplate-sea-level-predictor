import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress




def draw_plot():
    # Read data from file

    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot

    plt.scatter( df["Year"],df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    resA = linregress( df["Year"],df["CSIRO Adjusted Sea Level"])
    x1 = np.arange(df['Year'].min(),2051,1)
    plt.plot(x1, resA.intercept + resA.slope*x1)


    # Create second line of best fit
    recent_data = df[df["Year"] >= 2000]
    resB = linregress( recent_data["Year"],recent_data["CSIRO Adjusted Sea Level"])
    x2 = np.arange(2000,2051,1)
    plt.plot(x2, resB.intercept + resB.slope*x2)

    # Add labels and title

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()