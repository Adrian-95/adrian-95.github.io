title: Climate data visualization with Python
date: 2020-08-15
author: Adrian
category: Data Visualization
tags: Data, Climate, Python

In the age of **Big Data**, visualization is essential for making sense of millions of rows of unsorted raw data. More often than not, your data will come as a text file, or an excel file with rows and collumns. Here is an example of temperature anomaly data from an .xlsx file:

>Global temperature anomaly data come from the Global Historical Climatology Network-Monthly (GHCN-M) data set and International Comprehensive Ocean-Atmosphere Data Set (ICOADS), which have data from 1880 to the present. These two datasets are blended into a single product to produce the combined global land and ocean temperature anomalies. The available timeseries of global-scale temperature anomalies are calculated with respect to the 20th century average, while the mapping tool displays global-scale temperature anomalies with respect to the 1981-2010 base period.

```

Global Land and Ocean Temperature Anomalies	 January-December
Units: Degrees Celsius	
Base Period: 1901-2000	
Missing: -999	
Year	Value
1880	-0.12
1881	-0.08
1882	-0.1
1883	-0.18
1884	-0.27
1885	-0.25
1886	-0.24
1887	-0.28
1888	-0.13
1889	-0.09
1890	-0.34
1891	-0.25
1892	-0.31
1893	-0.33
1894	-0.3
1895	-0.24
1896	-0.09
1897	-0.1
1898	-0.27
1899	-0.15
1900	-0.07
1901	-0.15
1902	-0.26
1903	-0.37
1904	-0.46
1905	-0.28
1906	-0.21
1907	-0.38
1908	-0.43
1909	-0.45
...
2020    1.14`

```
At first glance, you may get a general idea of what this data is about. On the left column you clearly have years, and on the right you have what appears to be temperature anomalies. But this is not good enough if you wish to understand and interpret the data. 

Python provides great tools for data processing, plotting and visualization. For the example above we shall use `pandas` for reading and sorting the .xlsx file and `matplotlib` to create a 2D plot.

The first step is to import the `pandas` module and read the file.

```
import pandas
df = pandas.read_excel('C:/Users/Public/data.xlsx', skiprows=4)
print(df.columns)
x = df['Year'].values
y = df['Value'].values
```
Notice that we are skipping the first 4 rows since the columns are on the 5th row. Let's print the columns from our table and see if the file loaded correctly

So far so good, next we shall assign the two columns to x and y axes.

Now that we have our data loaded and assigned to variables, we can import matplotlib and create a plot.

```
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly Value')
plt.savefig('C:/Users/Public/climatedata.png', dpi=500)
```
![climateplot][climateplot]
[climateplot]: {static}/pages/images/climateplot.png

So now we have an x-y scatter plot of temperature anomalies versus time. This is obviously much better than analysing raw data and the overall warming trend can be seen clearly. But this plot is rather simple, it can be made better with some customization.