# Example heatmap was built for 'flights' dataset from the seaborn package

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("ticks")

flights_data = sns.load_dataset("flights")
flights_data_pt = flights_data.pivot_table(values='passengers', index='year', columns='month')

plot_3 = sns.heatmap(data=flights_data_pt, cmap="rocket")
plot_3.set(xlabel="Month", ylabel="Year",
           title="Airline passenger data (\"flights\" dataset)")
plt.show()