import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_excel('Girl Scout Cookie Goals.xlsx', header=None)

# Transpose the DataFrame
dataset_t = dataset.transpose()

# Set the first row as header
dataset_t.columns = dataset_t.iloc[0]

# Drop the first row as it's now the headers
dataset_t = dataset_t[1:]

# Cookie List
cookies = dataset_t.columns.values[1:]
num_cookies = len(cookies)

# Create line chart
i = 0
color = ['green', 'purple', 'brown', 'tan', 'yellow', 'blue', 'brown']
while i < num_cookies: 
  x = dataset_t["Dates"]
  y = dataset_t[cookies[i]]
  plt.subplot(4, 2, i+1)
  plt.plot(x, y, linewidth=3, color=color[i])
  plt.ylabel('Sales')
  plt.title(cookies[i])
  plt.ylim(bottom=0, top=50)
  ax = plt.gca()
  ax.xaxis.set_visible(False)
  i += 1

plt.subplots_adjust(hspace=0.5)
plt.suptitle('Girl Scout Cookie Sales Dashboard', fontsize=24)

plt.show()