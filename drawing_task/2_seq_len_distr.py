# Example plot was built for 'ssu_15mers.fa' file from the resourses of the BBTools (BBMap version 38.75)

import matplotlib.pyplot as plt
import seaborn as sns

# Get list of reads lengths from the indicated fasta file
path_to_input_fastq_file = input("Write path to input reads: ")
reads_lengths = []

input_fastq_file = open(path_to_input_fastq_file, 'r')

for line in input_fastq_file:
    if line.startswith('>') == False:
        reads_lengths.append(len(line))

input_fastq_file.close()

# Visualize reads length distribution
sns.set_style("ticks")
plot_2 = sns.displot(reads_lengths, kde=True, color='y')
plot_2.set(xlabel="Sequence length (bp)", ylabel="Count",
           title="Sequence length distribution")
plt.show()