# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:51:20 2023

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = pd.read_csv('C://Users//DELL//Downloads//police-locals//police-locals//police-locals.csv')

x = data['city']
y1 = data['police_force_size']
y2 = data['non-white']
y3 = data['white']
y4 = data['black']
y5 = data['hispanic']
y6 = data['asian']
y7 = data['all']

# Plotting the lines

plt.plot(x, y2, label='non-white')
plt.plot(x, y3, label='white')
plt.plot(x, y4, label='black')
plt.plot(x, y5, label='hispanic')
plt.plot(x, y6, label='asian')
plt.plot(x, y7, label='all')



# Adding labels and title
plt.xlabel('city')
plt.ylabel('police_force_size')
plt.title('Multiple Line Plot')

# Adding legend
plt.legend()

# Display the plot
plt.show()



x = data['city']
y = data['police_force_size']

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y2, alpha=0.5, label='non-white')
plt.scatter(x, y3, alpha=0.5, label='white')
plt.scatter(x, y4, alpha=0.5, label='black')
plt.scatter(x, y5, alpha=0.5, label='hispanic')
plt.scatter(x, y6, alpha=0.5, label='asian')
plt.scatter(x, y7, alpha=0.5, label='all')


# Adding labels and title
plt.xlabel('city')
plt.ylabel('police_force_size')
plt.title('Scatter Plot of Police_locals')

# Adding legend
plt.legend()

# Display the scatter plot
plt.show()

numerical_data = data['police_force_size']
numerical_data1 = data['white']
numerical_data2 = data['black']
# Plotting the histogram
plt.figure(figsize=(10, 6))

plt.hist(numerical_data1, bins=30, color='orange', edgecolor='black', alpha=0.7)
plt.hist(numerical_data2, bins=30, color='pink', edgecolor='black', alpha=0.7)

# Adding labels and title
plt.xlabel('police_force_size')
plt.ylabel('all')
plt.title('Histogram of Police_locals')

# Adding legend
plt.legend()

# Display the histogram
plt.show()

