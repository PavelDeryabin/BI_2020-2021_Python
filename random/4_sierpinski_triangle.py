import random
import matplotlib.pyplot as plt
import seaborn as sns

def get_dots_for_sierpinski_trianle(n):
    initial_dots = [[0.0, 0.0], [0.5, 1.0], [1.0, 0.0]]
    driving_dot = [0.25, 0.5]
    next_dot = random.choice(initial_dots)
    dots = []

    for i in range(n):
        next_x = (driving_dot[0] + next_dot[0]) / 2
        next_y = (driving_dot[1] + next_dot[1]) / 2

        dots.append([next_x, next_y])
        driving_dot = [next_x, next_y]
        next_dot = random.choice(initial_dots)

    return dots

dots = get_dots_for_sierpinski_trianle(100000)

sns.scatterplot(*zip(*dots), s=10, color=".2")
plt.show()