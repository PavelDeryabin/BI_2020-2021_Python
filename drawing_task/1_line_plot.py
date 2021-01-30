# Example plot was built for 'flights' dataset from the seaborn package

import matplotlib.pyplot as plt
import seaborn as sns

flights_data = sns.load_dataset("flights")
sns.set_style("ticks") # Setting

plot_1 = sns.lineplot(x="year",
                      y="passengers",
                      hue="month",
                      palette="RdYlGn",
                      data=flights_data)

plot_1.set(xlabel="Year", ylabel="Number of passengers",
           title="Monthly airline passenger data\n(\"flights\" dataset)")
plot_1.legend(title="Month", frameon=False)

plt.show()



