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

#Calculate the total sales for each cookie
total_sales = dataset_t[cookies].sum()

# Create dashboard
def plot_dashboard():
  # Create line charts
  i = 0
  color = ['green', 'purple', 'brown', 'tan', 'yellow', 'blue', 'brown']
  while i < num_cookies: 
    x = dataset_t["Dates"]
    y = dataset_t[cookies[i]]
    plt.subplot(4, 2, i+1)
    plt.plot(x, y, linewidth=2, color=color[i])
    plt.ylabel('Sales')
    plt.title(cookies[i])
    plt.ylim(bottom=0, top=50)
    ax = plt.gca()
    ax.xaxis.set_visible(False)
    i += 1
  
  plt.subplots_adjust(hspace=0.5)
  plt.suptitle('Girl Scout Cookie Sales Dashboard', fontsize=24)
  
  
  # Create a bar chart for total sales
  x = range(len(cookies))
  plt.subplot(4, 2, 8)
  plt.bar(x, total_sales, color=color)
  plt.xticks([])
  plt.title('Total Cookie Sales')
  plt.xlabel('Cookie Type')
  plt.ylabel('Total Sales')
  
  plt.show()

plot_dashboard()