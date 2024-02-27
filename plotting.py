import pandas as p
import matplotlib.pyplot as plt

df=p.read_csv("G:/studentData.csv")
#print(df)
#df.plot()
#plt.show()

#Scattreing of data
#df.plot(kind='scatter',x='student Name',y='marks')
#plt.show()

#Histogram/bar Graph
df['marks'].plot(kind='hist')
plt.show()

#pie chart
#df['marks'].plot(kind='pie')
#plt.show()