# Name: Francis Chuks
# Student ID: 2306408

import random
import matplotlib.pyplot as plt

# 1) Change myID to your own student ID. This MUST be your student ID.
myID = "2306408"

# 2) User input validation
# The snippet should ask for an integer until the entered number is >= 50.
while True:
    try:
        varCount = int(input("Enter an integer (>= 50): "))
        if varCount >= 50:
            break
        else:
            print("Please enter a number greater than or equal to 50.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# 3) randSeedNum
# s_d is calculated by summing all digits in the student ID
s_d = sum(int(d) for d in myID)

# BUG FIX: The variable was wrongly named 'ssd' instead of 's_d'
random.seed(s_d)

# 4) Random list creation
data = [random.randint(1, 200) for _ in range(varCount)]

# Compute the sum of data
data_sum = sum(data)

# Compute the mean of data
data_mean = data_sum / len(data)

# Compute the minimum and maximum of data
data_min = min(data)
data_max = max(data)

# Print the results with corrected formatting
print(f"Sum: {data_sum}, Mean: {data_mean:.2f}, Min: {data_min}, Max: {data_max}")

# Plot a histogram of data
plt.hist(data, bins=10, edgecolor='black')
plt.title("Histogram of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# Commentary:
# My script collects a valid user input (>= 50), it also sets a seed based on my student ID,
# generates a list of random integers, performs basic statistics, and graphs the distribution.
