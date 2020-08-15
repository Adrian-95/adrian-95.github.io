title: Past climate data visualization with Python
date: 2020-08-15
author: Adrian
category: Data Visualization
tags: Data, Climate, Python

In the age of "Big Data", visualization is essential for making sense of millions of rows of unsorted raw data. More often than not, your data will come as a text file, or an excel file with rows and collumns. Here is an example of temperature anomaly data from a .csv file:

'Global Land and Ocean Temperature Anomalies	 January-December
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
...'

At first glance, you may get a general idea of what this data is about. On the left column you clearly have years, and on the right you have what appears to be temperature anomalies. But this is not good enough if you wish to understand and interpret the data. 

Python provides great tools for data processing, plotting and visualization. For the example above we shall use 'pandas' for reading and sorting the .csv file and "matplotlib" to create a 2D plot.