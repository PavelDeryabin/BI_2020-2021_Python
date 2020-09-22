print("Hello, this is converter of common temperature measure units!")
print("Please, provide one value and its unit measure (C, K, F):")

value = float(input())
measure = input()

if measure == "C":
    print("Results: " + str(round((value + 273.15), 2)) + "K, " + str(round((value * (9 / 5) + 32), 2)) + "F")
elif measure == "K":
    print("Results: " + str(round((value - 273.15), 2)) + "C, " + str(round(((value - 273.15) * (9 / 5) + 32), 2)) + "F")
elif measure == "F":
    print("Results: " + str(round(((value - 32) * 5 / 9), 2)) + "C, " + str(round((((value - 32) * 5 / 9) + 273.15), 2)) + "K")
else:
    print("Please provide correct units measure and try again")

# another edit for conflict
