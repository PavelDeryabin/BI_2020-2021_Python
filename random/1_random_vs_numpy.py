import time
import numpy
import random
import matplotlib.pyplot as plt
import seaborn as sns

numbers_of_calls_list = [x for x in range(1000)]
random_times = []
numpy_random_times = []

for call_number in numbers_of_calls_list:

    start_time = time.time()
    for _ in range(call_number):
        random.uniform(0, 1)
    random_times.append(time.time() - start_time)

    start_time = time.time()
    for _ in range(call_number):
        numpy.random.uniform(0, 1)
    numpy_random_times.append(time.time() - start_time)

sns.set_style("whitegrid")
sns.lineplot(x=numbers_of_calls_list, y=random_times)
sns.lineplot(x=numbers_of_calls_list, y=numpy_random_times)
plt.title('Comparison of running time for random numbers calculation')
plt.xlabel('Number of calls')
plt.ylabel('Calculation time (s)')
plt.legend(['random module', 'numpy module'])
plt.show()