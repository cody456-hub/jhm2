import pandas as pd
import matplotlib.pyplot as plt 


data = {
'Month_a': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
'Sales_a': [380, 400, 660, 800, 900, 1200, 1600, 2200, 1500, 1100, 600, 250]
}
df = pd.DataFrame(data)
df.to_csv('sales.csv', index=False)
df = pd.read_csv('sales.csv')


a = df['Month_a']
b = df['Sales_a']

plt.bar(a,b,color = 'green',width=0.5)
plt.title("Bar Chart of ice-cream Sales")
plt.xlabel("Month")
plt.ylabel("Sales(in thousand dollars)")

plt.show()