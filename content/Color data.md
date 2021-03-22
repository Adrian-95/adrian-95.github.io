title: Extracting color data from sedimentary cores
date: 2021-03-22
author: Adrian
category: Data Analysis
tags: Data, Climate, Geology

Understanding paleoclimatic conditions on Earth from millions of years ago remains a serious challenge, a problem that geoscientists have wrestled with for the past several decades. There are many past climate proxies which can help us understand the archaic climate of the Earth, such as isotopes from ice cores or fossils which relay the paleoenvironment and past temperatures based on the distribution of species. 

Sedimentary cores are among the few proxies which can be classified as **hard data**, thus extremely valuable to geoscientists. Alas, they are expensive to produce and therefore quite rare as well. There is a lot of information that a logging geologist can derive from core observations, mostly related to the properties of the rocks. But even moreso, an extensive core log can reveal certain patterns and cyclicities which may be correlated to environmental changes or climatic shifts in the past. Nonetheless, observing, let alone interpreting these events is no small task, but fortunately, modern software provides the ability to process and analyze quantitative data much more effectively. This article will convey one way to extract color data from high-resolution images of sedimentary cores.



### Extracting Color Data - Creating a Picture Log 

Assuming you want to cover the entirety of your studied succession, you will probably have a few dozen core boxes, possibly more. You will photograph the whole succession, but in order to properly sample the core you must put it back together in a chronological manner. The simplest way to do this is to cut the core material from your photos and reconstruct the core in an image editing software such as **Adobe Illustrator**. 

With basic image editing skills, this is an easy task, but you will want to keep 2 things in mind as you do this. First, you should make a scale and keep checking that the picture log matches the depth of your paper log as you add the cropped core pictures. Secondly, make sure the cropped core pictures have more or less the same dimensions and realistically depict your core succession. The scale will also help you in this sense, because the picture log will be a bit off in case some of your images are shrunken or enlarged. 

In the end, you want to have a continuos picture log of your studied succession, as if all your core was in a single, really long box. This will make sampling much easier, and since you have the scale too now you can easily keep track of your sampling rate. On a final note, try your best to keep image quality high as you process your core photos. 



### Extracting Color Data - Sampling 

Naturally, the next step is to take color data samples from the core. This can be done in several ways, but since we are working with pictures of cores in this case we must do the sampling digitally. For this purpose, we shall use **ImageJ**. In this software, you can select an area in any given picture and calculate the average R, G and B values of the selected area. For a good resolution, it is a good idea to sample every 2.5 cm on average, although you may choose a different sampling rate depending on how much core material you have.

![colorsampling][colorsampling]
[colorsampling]: {static}/pages/images/colorsampling.jpg
*Example of color data sampling in ImageJ*



##### Step by step ImageJ sampling procedure: 

1. Save your picture log as a jpeg and open it in ImageJ
2. Go to Image > Color and select "Make Composite". This will split the image in R, G and B color channels
3. Zoom in on you picture log with the lens tool. Start at maximum depth.
4. Select the rectangle or the oval tool to begin taking your first samples. Use the scale to make sure you more or less respect your chosen sampling rate.
5. Once you select your first sampling area, press "CTRL-T" to save the sample. This will open a new window called ROI manager where you can see all your samples. I recommend you check the "Show All" and "Labes" boxes so that you can see all your samples on the core. Simply repeat the process for each new sample. 
Tip: you can also move the rectangle/oval with your arrow keys.
6. Once you have a decent number of samples or regions of interest (ROI), it is a good idea to save your progress. First, select them all with shift-click. 
7. Go to More > Multi Measure. A new window will appear, make sure you measure all your samples and check the "One Row per Slice" box. 
8. A new window will open with as many columns as samples you submitted, and 3 lines for each column representing the average R, G and B values for each of your samples.
9. Save the results in a .txt file and repeat the process from Step 4 until you sampled your entire succession.



![samplingresults][samplingresults]
[samplingresults]: {static}/pages/images/samplingresults.jpg
*The results should look something like this. The rows show the R, G and B values for each measured sample.*



### File Processing 

It is not ideal to have your color data in .txt files. The next step is to transpose the data and save it in excel. In order to do this, we shall use the **PAST** software

To do this, simply open your .txt files one by one in the PAST software, go to Edit > Rearrange and select the Transpose function. Your data matrix is now transposed with RGB in columns and samples in lines. Finally, save the file and reopen it in excel. It is a good idea to add the coresponding depth for each one of your samples, as you will need it for plotting the data later. Assuming you followed your chosen sampling rate, you can write an excel formula and quickly set the depth for your samples (but watch out for gaps!).

You should now have between several hundreds to several thousands of RGB color data samples, depending on how much core material you have available. You are now very close to being ready to plot and interpret your color data. We shall cover the last steps of data processing and interpretation in the next article. 

You can find the download links for the freeware (ImageJ and PAST) on our **resources** page.



