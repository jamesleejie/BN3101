import matplotlib.pyplot as plt
import numpy as np
from itertools import count
import time

# Define a function to simulate data
def get_data():
    for i in count(1):
        yield i  # You can replace this with your data source

# Create a color map (you can define your own color map)
colors = plt.cm.get_cmap('cool', 100)  # Use 'cool' colormap with 100 colors

# Create a figure and axis
fig, ax = plt.subplots(figsize=(6, 2))

# Initialize the plot with an initial value
current_level = next(get_data())
current_color = colors(current_level / 100)
marker = ax.plot(current_level, 0, marker='o', markersize=10, color=current_color)[0]

# Customize the plot
ax.set_xlim(0, 100)
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xlabel("Current Level")
ax.set_yticks([])  # Hide the y-axis

plt.ion()  # Enable interactive mode

try:
    for i in get_data():
        current_level = i
        current_color = colors(current_level / 100)
        
        # Update the marker position and color
        marker.set_xdata(current_level)
        marker.set_color(current_color)
        
        plt.pause(0.1)  # Pause briefly to update the plot

except KeyboardInterrupt:
    pass

plt.ioff()  # Disable interactive mode

# Close the plot when done
plt.show()
