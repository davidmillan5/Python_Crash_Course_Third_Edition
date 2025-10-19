import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.

while True:
    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()


    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=4)
    ax.set_aspect('equal')

    # Emphasize the starting point (green) and the ending point (red).
    ax.scatter(0, 0, c='green', edgecolors='none', s=100, label='Start')  # start point
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100, label='End')  # end point

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

