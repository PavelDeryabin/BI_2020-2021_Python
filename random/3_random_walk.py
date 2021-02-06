import numpy
import random
import matplotlib.pyplot as plt
import seaborn as sns

number_of_steps = 100000

x, y = numpy.zeros(number_of_steps), numpy.zeros(number_of_steps)

for i in range(1, number_of_steps):
    direction = random.randint(1, 4) # !!! random and numpy.random dramatically differ
    if direction == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif direction == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif direction == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1

sns.set_style("whitegrid")
plt.plot(x, y)
plt.title('Random walking 2D')
plt.show()