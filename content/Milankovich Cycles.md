title: Global climate controls: Milankovich Cycles
date: 2020-08-31
author: Adrian
category: Data Visualization
tags: Climate, Geology, Python

Earth's climate has been closely monitored for the past century with direct measurements and observation of climate components such as precipitation and temperature. Analyzing past climate records is a more difficult endeavor due to the lack of such direct data. In order to reconstruct past climate conditions, scientists must rely on various proxies that are sensitive to climatic and environmental changes. Such proxies may be oxygen and hydrogen isotopes preserved in ice cores or fossil remains from marine organisms such as belemnites or foraminifera, preserved in the geological record. 

## Milankovitch Cycles

In the 19th century, a geologist named Jean Louis Aggasiz made several observations based on glacial deposits which indicated the presence of a massive ice sheet which covered much of Europe. This raised many questions, such as what are the factors that control the coming and going of ice ages. In the 20th century however, a Serbian scientist named Milutin Milankovitz proposed and explanation for the climatic shifts that control the ice ages. He argued that the changes are likely due to variations in the Earth's orbit around the sun, which controls insolation, the amount of energy received from the sun. These cycles were thereafter called Milankovich cycles.

Milankovich defined three key parameters for orbital cycle calculations: eccentricity, obliquity and the precession of the spin axis.

### Eccentricity

Earth's orbit is not a perfect circle, but has a slightly eliptical shape due to the gravitational pull of nearby planets. Eccentricity is therefore the measure of variations of the orbital shape.

![eccentricity][eccentricity]
[eccentricity]: {static}/pages/images/eccentricity.jpg
Source: Ruddiman, 2008

Earth's distance from the Sun changes depending on its position on the eliptical orbit. Subsequently, this position affects the amount of solar radiation Earth receives, especially at perihelion (the position at which the Earth is closest to the Sun) and aphelion (the position at which the Earth is farthest away from the Sun).

### Obliquity

The Earth rotates around an invisible axis that passes through its poles. Obliquity measures the effect of increased tilt on poles. Earth's tilt also has a significant control on insolation, and therefore the coming and going of ice ages.

Ice sheets usually develop when the axial tilt is small and summer insolation is low. The poles are therefore less directly towards the Sun.

![obliquity1][obliquity1]
[obliquity1]: {static}/pages/images/obliquity1.jpg
Source: Ruddiman, 2008

On the other hand, Ice sheets shrink when axial tilt is high and summer insolation is high. 

![obliquity2][obliquity2]
[obliquity2]: {static}/pages/images/obliquity2.jpg
Source: Ruddiman, 2008

### Axial precession

In addition to spinning about its invisible axis, the Earth's spin axis also wobbles gradually in different directions through time, as a result of the gravitation pull of the Sun and Moon. This is known as Axial Precession.

![precession][precession]
[precession]: {static}/pages/images/precession.jpg
Source: Ruddiman, 2008

The Earth's eliptical orbit is also subject to precession, although it is slower than axial precession. Both motions alter the position of the solstices and equinoxes.

## Milankovich Cycles moddeling in Python

The variability of Earth's orbital parameters of eccentricity, obliquite and precession is quite predictable. Let's build a cyclicity model that displays the variability of milankovich cycles over the past 2 Million years.

> Data obtained from J. Laskar et al (2004) A long term numerical solution for the insolation quantities of the Earth. Astronomy and Astrophysics 428, 261-285, DOI: 10.1051/0004-6361:20041335

```
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pandas 
# Read the datafile with Pandas
mkdata=pandas.read_excel('C:/Users/Public/mkdata.xlsx', skiprows=7)
print (mkdata.columns)

>Index(['time', 'eccentricity', 'obliquity', 'perihelion', 'insolation',
       'global.insolation'],
      dtype='object')


# now to plot the orbital parameters
# Eccentricity
fig=plt.figure(1,(10,10)) 
fig.add_subplot(311) 
plt.plot(mkdata['time'],mkdata['eccentricity'],c ='r')
plt.ylabel('Eccentricity')

# Obliquity
fig.add_subplot(312)
plt.plot(mkdata['time'],mkdata['obliquity'],c ='g')
plt.ylabel('Obliquity')

# Precession
fig.add_subplot(313)
plt.plot(mkdata['time'],mkdata['eccentricity'] * np.sin(mkdata['perihelion']),c ='b')
plt.ylabel('Precession')
plt.xlabel('Age (ka)'); #Unit: 1 ka = 1000 years
plt.savefig('C:/Users/Public/mkplot1.png', dpi=500)
```

![mkplot1][mkplot1]
[mkplot1]: {static}/pages/images/mkplot1.png

This model clearly shows the different cyclicities of the orbital parameters. The real question is how do these relate to the amount of insolation received by Earth. Let us make an additional plot for Insolation received at 65N summer solstice.

```
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import pandas 
mkdata=pandas.read_excel('C:/Users/Public/mkdata.xlsx', skiprows=7)
# Insolation
fig=plt.figure(1,(10,4)) 
plt.plot(mkdata['time'],mkdata['insolation'],c ='y')
plt.ylabel('Insolation')
plt.xlabel('Age (ka)');
plt.savefig('C:/Users/Public/mkplot2.png', dpi=500)
```

![mkplot2][mkplot2]
[mkplot2]: {static}/pages/images/mkplot2.png

There is definitely a correlation between these models, but how do they relate to ice ages? Can this data relay the exact timing and extent of past glaciations or is there more to the story? We shall explore the topic further and discuss the role of marine fossils in past climate models.