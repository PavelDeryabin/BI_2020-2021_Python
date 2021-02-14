import itertools

n = int(input("Indicate sequences length limit: "))

def generate_sequences_of_given_len(n):
    for i in range(1, n+1):
        xs = list(itertools.product(['A', 'T', 'C', 'G'], repeat=i))
        yield from list(map(''.join, xs))

print(generate_sequences_of_given_len(n)) # <generator object generate_sequences_of_given_len at 0x7ff1d6a84ba0>
print(list(generate_sequences_of_given_len(n))) # ['A', 'T', 'C', 'G', 'AA', 'AT', 'AC', 'AG' ...

