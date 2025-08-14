# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Step 1: Generate 1,000 random numbers from a normal distribution
data_normal = np.random.normal(loc=0, scale=1, size=1000)

# Step 2: Plot a histogram
sns.histplot(data_normal, kde=False, stat='density', bins=30, color='skyblue', label='Data Histogram')

# Step 3: Calculate descriptive statistics
mean = np.mean(data_normal)
median = np.median(data_normal)
std_dev = np.std(data_normal)

# Step 4: Fit a normal distribution curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)
plt.plot(x, p, 'r', linewidth=2, label='Normal Curve Fit')

# Add title and labels
plt.title('Histogram of Normally Distributed Data with Normal Curve')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

# Print Descriptive Stats
print(f"Mean: {mean:.4f}")
print(f"Median: {median:.4f}")
print(f"Standard Deviation: {std_dev:.4f}")
