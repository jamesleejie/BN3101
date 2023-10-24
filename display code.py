import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import time 

# Create a figure and axis
fig, ax = plt.subplots()

# Define the color ranges
color_ranges = [(0, 10, 'red'), (10, 34, 'yellow'), (34, 90, 'green'), (90, 100, 'red')]

#Define box height
box_height = 0.5

# Create rectangles for each color range
for start, end, color in color_ranges:
    ax.add_patch(patches.Rectangle((start, 0.25), end - start, box_height, facecolor=color))

# Customize the plot
ax.set_xlim(0, 100)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_xlabel("")
ax.set_yticks([])  # Hide the y-axis
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

#Text for the good and average zone
text_between = "Good Zone"
ax.text(64, 0.80, text_between, ha='center', va='center', fontsize=10, weight = 'bold', color='green')

text_between = "Average Zone"
ax.text(22, 0.80, text_between, ha='center', va='center', fontsize=10, weight = 'bold', color='orange')

real_time_data = 95
# for i in range():
#     i = i*16 +10 
#     real_time_data = i

#Creating arrow 
arrow = patches.FancyArrow(real_time_data, 0.25, 0, 0.46, width=0.2, head_width=1.6, head_length=0.04, fc='black', ec='black')
ax.add_patch(arrow)

#Text describing current intensity
text = f'Current Exercise Intensity:\n {real_time_data}'
ax.text(real_time_data, 0.16, text, ha='center', va='center', fontsize=10)

#text to show in each zone
if 10 < real_time_data <= 34:
   text_between = "You can push a little harder!"
   ax.text(50, 0.05, text_between, ha='center', va='center', fontsize=20, weight = 'bold', color='orange')

elif 34< real_time_data <= 90:
   text_between = "Good job! Keep it up!"
   ax.text(50, 0.05, text_between, ha='center', va='center', fontsize=20, weight = 'bold', color='green')

elif real_time_data < 10:
   background_rect = patches.Rectangle((0, -0.1), 100, 0.2, facecolor='red', edgecolor='none')
   ax.add_patch(background_rect)
   text_between = "You are not working enough!"
   ax.text(50, 0.05, text_between, ha='center', va='center', fontsize=20, weight = 'bold', color='white')
   def toggle_visibility():
    if background_rect.get_visible():
        background_rect.set_visible(False)
    else:
        background_rect.set_visible(True)
    fig.canvas.draw_idle()
   while True:
      toggle_visibility()
      plt.pause(1)

else:
   background_rect = patches.Rectangle((0, -0.1), 100, 0.2, facecolor='red', edgecolor='none')
   ax.add_patch(background_rect)
   text_between = "You need to stop immediately!"
   ax.text(50, 0.05, text_between, ha='center', va='center', fontsize=20, weight = 'bold', color='white')
   def toggle_visibility():
    if background_rect.get_visible():
        background_rect.set_visible(False)
    else:
        background_rect.set_visible(True)
    fig.canvas.draw_idle()
   while True:
      toggle_visibility()
      plt.pause(1)


# Show the plot
plt.show()


