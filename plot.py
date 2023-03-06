import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import arff

dataset = 'cardio.arff'
# Load the .arff dataset into a pandas DataFrame
data, meta = arff.loadarff(dataset)
df = pd.DataFrame(data)
df['Class'] = df['Class'].astype(int)
# Sort the tuples based on the target attribute 'CLASS'
df = df.sort_values('Class')

# Select the target attribute name to plot
target_attr_name = 'Class'
x_label = 'FHR pattern class code'
y_label = 'Frequency'

# Plot the distribution/histogram of values in the target attribute
plt.hist(df[target_attr_name].dropna(), bins=10)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()
