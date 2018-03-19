"""
Source:
https://stackoverflow.com/questions/37517936/matplotlib-scatterplot-open-image-corresponding-to-point-which-i-click
"""
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, 'o')


def onclick(event):
    ix, iy = event.xdata, event.ydata
    print("I clicked at x={0:5.2f}, y={1:5.2f}".format(ix, iy))

    # Calculate, based on the axis extent, a reasonable distance
    # from the actual point in which the click has to occur (in this case 5%)
    ax = plt.gca()
    dx = 0.05 * (ax.get_xlim()[1] - ax.get_xlim()[0])
    dy = 0.05 * (ax.get_ylim()[1] - ax.get_ylim()[0])

    # Check for every point if the click was close enough:
    for i in range(len(x)):
        if (x[i] > ix - dx and x[i] < ix + dx and y[i] > iy - dy and y[i] < iy + dy):
            print("You clicked close enough!")


cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
