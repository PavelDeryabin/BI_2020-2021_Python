import time
import numpy
import random
import matplotlib.pyplot as plt
import seaborn as sns

def is_sorted(list):
    flag = 1
    for i in range(len(list) - 1):
        if list[i] <= list[i+1]:
            flag = flag * 1
        else:
            flag = flag * 0
    return bool(flag)

def bogosort(list):
    while not is_sorted(list):
        random.shuffle(list)
    #return list

time_measurements = []
list_sizes = [x for x in range(11)]
measurements_means = []
measurements_errors = []

for list_size in list_sizes:
    for repeat in range(5):
        list_to_check = random.sample(range(10), list_size)
        start_time = time.time()
        bogosort(list_to_check)
        time_measurements.append(time.time() - start_time)
    measurements_means.append(numpy.mean(time_measurements) / 5)
    measurements_errors.append(numpy.std(time_measurements) / 5)
    time_measurements = []

sns.set_style("whitegrid")
sns.barplot(x=list_sizes, y=measurements_means, color="blue", alpha=0.2)
plt.errorbar(x=list_sizes, y=measurements_means, yerr=measurements_errors)
plt.title('The \'bogosort\' algorithm running time\ndepending on the size of the sorted list')
plt.xlabel('Sorted list size')
plt.ylabel('Running time (s)')
plt.show()