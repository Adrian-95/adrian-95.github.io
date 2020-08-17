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

The first step is to import the `pandas` module and read the file. Afterwards the Year column will be assigned to the x axis and the Value column will be assigned to the y axis.

```
import pandas
df = pandas.read_excel('C:/Users/Public/data.xlsx', skiprows=4)
print(df.columns)
x = df['Year'].values
y = df['Value'].values
```
Notice that we are skipping the first 4 rows since the columns are on the 5th row. Now that we have our data loaded and assigned to variables, we can import matplotlib and create a plot.

```
import matplotlib.pyplot as plt
plt.scatter(x, y)
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly Value')
plt.savefig('C:/Users/Public/climateplot.png', dpi=500)
```
![climateplot][climateplot]
[climateplot]: {static}/pages/images/climateplot.png

So now we have an x-y scatter plot of temperature anomalies versus time. This is obviously much better than analysing raw data and the overall warming trend can be seen clearly. Lets customize the plot by changing the figure size as well as making the data points smaller and red instead of blue.

Finally, the code will look like this

```
import pandas
import matplotlib.pyplot as plt
df = pandas.read_excel('C:/Users/Public/data.xlsx', skiprows=4)
print(df.columns)
x = df['Year'].values
y = df['Value'].values
plt.figure(figsize=(10,5))
plt.scatter(x, y, s=10, c ='r', marker='o')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly Value')
plt.savefig('C:/Users/Public/climateplot2.png', dpi=500)
```

![climateplot2][climateplot2]
[climateplot2]: {static}/pages/images/climateplot2.png

There are many other types of plots and customization options available with matplotlib. You can choose between line plots, scatter plots histograms, three-dimensional plots, streamplots, bar charts, pie charts and much more, depending on what best fits your data.

## The power of Visualization ##

The possibilities for Data Visualization with Python are almost endless. Although we only made some simples 2D plots earlier, the information conveyed is pretty solid. You can go much further than that though, as you are about to see in the following example. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/7RygVNrKMs0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

This animation was made using Python and it displays a huge ammount of information in a very effective manner. The viewer sees the temperature anomalies for each country, in every year starting from 1880 all the way to 2017. As seen in the 2D plots, the temperature anomalies get more and more significant starting from 1960, and as you get in the 2000s almost every country has a big red circle, which signifies a positive temperature anomaly. 

There is much more to be done with Python, but these examples can be a good inspiration for other big data projects.