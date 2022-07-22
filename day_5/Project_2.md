# Group Project 2: User interface to display the JB2008 and TIE-GCM models and comparison
Description: In the project, the students will work together to analyze and visualize the difference in predicted densities by the JB2008 density model and the TIE-GCM density model by creating functions that display differences in the models.


## Task 1: Download the dst index for the year 2002 from the NASA OmniWeb database
For this work, we are only interested in evaluating the differences between the two density models during high space weather events (i.e. large dst value). You first need to select a time period where the dst index is high in the year 2002 (including 5 hours prior and 5 hours after the high space weather event). *Note: as the density data are in hourly format, we will first need to convert the high temporal resolution of the dst index into a lower temporal resolution of an hour. This can be achieved using data slicing.*


## Task 2: Extract and plot the predicted densities at 450 km the selected period of high space activity (dst)
After identifying the time period of interest, plot the densities predicted by JB2008 and TIE-GCM for these periods at an altitude of 450 km. *Note: You will have to use 3D interpolation in order to obtain the correct density values.*


