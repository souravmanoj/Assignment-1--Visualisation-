# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 11:13:07 2023

@author: soura
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_line():
    # Load data for line plot
    line_data = pd.read_excel(r"C:\\Users\\soura\\OneDrive\\Desktop\\data\\line.xlsx", index_col=0)

    # Create line plot
    line_data.plot.line()
    plt.title("Malaria Cases by Country (2015-2020)")
    plt.xlabel("Year")
    plt.ylabel("Number of Cases")
    plt.show()


def plot_bar():
    # Load data for bar plot
    bar_data = pd.read_csv("C:/Users/soura/OneDrive/Desktop/data/bar.csv")

    # Create bar plot
    plt.bar(bar_data["Country"], bar_data["Malaria death"])
    plt.title("Malaria Deaths by Country")
    plt.xlabel("Country")
    plt.ylabel("Number of Deaths")
    plt.show()

def plot_scatter():
    # Load data for scatter plot
    scatter_data = pd.read_csv("C:\\Users\\soura\\OneDrive\\Desktop\\data\\scatered.csv")

    # Create scatter plot
    plt.scatter(scatter_data["Country"], scatter_data["Maleria Deaths(Age-70+)"])
    plt.title("Malaria Deaths (Age 70+) by Country")
    plt.xlabel("Country")
    plt.ylabel("Number of Deaths")
    plt.show()

if __name__ == "__main__":
    # Main program
    plot_line()
    plot_bar()
    plot_scatter()
