import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats

#treefile = open("C:\\Users\\nkolarik\\Desktop\\TomSawyer\\output\\November\\ENVI_LiDAR\\field_trees.csv", 'r')
treefile = open("C:\\Users\\nkolarik\\Desktop\\TomSawyer\\output\\July\\ENVI_LiDAR\\field_trees.csv", 'r')

tree_data = np.genfromtxt(treefile, delimiter = ",")

radius = 15
titles = ["RGB", "Green", "Red", "Red Edge", "NIR"]

x = tree_data[1:, 12]
y = tree_data[1:, radius]
x1 = y1 = range(0,31)


plt.subplot(321)
plt.scatter(x,tree_data[1:,15])
plt.title(titles[0])
plt.xlabel("Field Measurement")
plt.ylabel("Estimate")
plt.axis([0,10,0,10])
plt.plot(x1,y1, color = '0.5')

xlist = []
ylist = []
zipped = zip(x, y)
for pair in zipped:
    ## checking for nan vals in estimates
    if np.isnan(pair[1]) == 0:
        xlist.append(pair[0])
        ylist.append(pair[1])
##Statistical analysis
absresiduals = []
#residuals = []
res_sq = []
for i in range(0, len(xlist)):
    diff = ylist[i] - xlist[i]

    absresiduals.append(abs(diff))

## Squaring residuals- REMOVED PER DR STARDUST!
#for resid in residuals:
#	res_sq.append(resid**2)
	
	
sprmn_r, pval = (scipy.stats.mstats.spearmanr(xlist, ylist))
#rmse =  math.sqrt(sum(res_sq)/ (len(xlist)-1))
n = len(absresiduals)
mae = (sum(absresiduals))/ n
## adding txt to plots
plt.annotate("MAE = "+ str(round(mae,3)), xy = (6.5, 0.5))
plt.annotate("n = " + str(n), xy = (7.125,3.5))
plt.annotate("r = " + str(round(sprmn_r, 3)), xy = (7.25, 2.5))
plt.annotate("p = " + str(round(float(pval),3)), xy = (7.125, 1.5))
#plt.annotate(s = "a", xy = (0.3,9), fontweight = 'bold')
plt.annotate(s = "f", xy = (0.3,9), fontweight = 'bold')

radius = 18
y = tree_data[1:, radius]
plt.subplot(322)
plt.scatter(x,y, color = 'g')
plt.title(titles[1])
plt.xlabel("Field Measurement")
plt.ylabel("Estimate")
plt.axis([0,10,0,10])
plt.plot(x1,y1, color = '0.5')

xlist = []
ylist = []
zipped = zip(x, y)
for pair in zipped:
    ## checking for nan vals in estimates
    if np.isnan(pair[1]) == 0:
        xlist.append(pair[0])
        ylist.append(pair[1])
##Statistical analysis
absresiduals = []
#residuals = []
res_sq = []
for i in range(0, len(xlist)):
    diff = ylist[i] - xlist[i]

    absresiduals.append(abs(diff))

## Squaring residuals- REMOVED PER DR STARDUST!
#for resid in residuals:
#	res_sq.append(resid**2)
	
	
sprmn_r, pval = (scipy.stats.mstats.spearmanr(xlist, ylist))
#rmse =  math.sqrt(sum(res_sq)/ (len(xlist)-1))
n = len(absresiduals)
mae = (sum(absresiduals))/ n
## adding txt to plots
plt.annotate("MAE = "+ str(round(mae,3)), xy = (6.5, 0.5))
plt.annotate("n = " + str(n), xy = (7.125,3.5))
plt.annotate("r = " + str(round(sprmn_r, 3)), xy = (7.25, 2.5))
plt.annotate("p = " + str(round(float(pval),3)), xy = (7.125, 1.5))
#plt.annotate(s = "b", xy = (0.3,9), fontweight = 'bold')
plt.annotate(s = "g", xy = (0.3,9), fontweight = 'bold')

radius = 21
y = tree_data[1:, radius]
plt.subplot(323)
plt.scatter(x,y, color = 'r')
plt.title(titles[2])
plt.xlabel("Field Measurement")
plt.ylabel("Estimate")
plt.axis([0,10,0,10])
plt.plot(x1,y1, color = '0.5')

xlist = []
ylist = []
zipped = zip(x, y)
for pair in zipped:
    ## checking for nan vals in estimates
    if np.isnan(pair[1]) == 0:
        xlist.append(pair[0])
        ylist.append(pair[1])
##Statistical analysis
absresiduals = []
#residuals = []
res_sq = []
for i in range(0, len(xlist)):
    diff = ylist[i] - xlist[i]

    absresiduals.append(abs(diff))

## Squaring residuals- REMOVED PER DR STARDUST!
#for resid in residuals:
#	res_sq.append(resid**2)
	
	
sprmn_r, pval = (scipy.stats.mstats.spearmanr(xlist, ylist))
#rmse =  math.sqrt(sum(res_sq)/ (len(xlist)-1))
n = len(absresiduals)
mae = (sum(absresiduals))/ n
## adding txt to plots
plt.annotate("MAE = "+ str(round(mae,3)), xy = (6.5,0.5))
plt.annotate("n = " + str(n), xy = (7.125,3.5))
plt.annotate("r = " + str(round(sprmn_r, 3)), xy = (7.25, 2.5))
plt.annotate("p = " + str(round(float(pval),3)), xy = (7.125, 1.5))
#plt.annotate(s = "c", xy = (0.3,9), fontweight = 'bold')
plt.annotate(s = "h", xy = (0.3,9), fontweight = 'bold')

radius = 24
y = tree_data[1:, radius]
plt.subplot(324)
plt.scatter(x,y, color = 'magenta')
plt.title(titles[3])
plt.xlabel("Field Measurement")
plt.ylabel("Estimate")
plt.axis([0,10,0,10])
plt.plot(x1,y1, color = '0.5')

xlist = []
ylist = []
zipped = zip(x, y)
for pair in zipped:
    ## checking for nan vals in estimates
    if np.isnan(pair[1]) == 0:
        xlist.append(pair[0])
        ylist.append(pair[1])
##Statistical analysis
absresiduals = []
#residuals = []
res_sq = []
for i in range(0, len(xlist)):
    diff = ylist[i] - xlist[i]

    absresiduals.append(abs(diff))

## Squaring residuals- REMOVED PER DR STARDUST!
#for resid in residuals:
#	res_sq.append(resid**2)
	
	
sprmn_r, pval = (scipy.stats.mstats.spearmanr(xlist, ylist))
#rmse =  math.sqrt(sum(res_sq)/ (len(xlist)-1))
n = len(absresiduals)
mae = (sum(absresiduals))/ n
## adding txt to plots
plt.annotate("MAE = "+ str(round(mae,3)), xy = (6.5,0.5))
plt.annotate("n = " + str(n), xy = (7.125,3.5))
plt.annotate("r = " + str(round(sprmn_r, 3)), xy = (7.25, 2.5))
plt.annotate("p = " + str(round(float(pval),3)), xy = (7.125, 1.5))
#plt.annotate(s = "d", xy = (0.3,9), fontweight = 'bold')
plt.annotate(s = "i", xy = (0.3,9), fontweight = 'bold')

radius = 27
y = tree_data[1:, radius]
plt.subplot(325)
plt.scatter(x,y, color = 'purple')
plt.title(titles[4])
plt.xlabel("Field Measurement")
plt.ylabel("Estimate")
plt.axis([0,10,0,10])
plt.plot(x1,y1, color = '0.5')

xlist = []
ylist = []
zipped = zip(x, y)
for pair in zipped:
    ## checking for nan vals in estimates
    if np.isnan(pair[1]) == 0:
        xlist.append(pair[0])
        ylist.append(pair[1])
##Statistical analysis
absresiduals = []
#residuals = []
res_sq = []
for i in range(0, len(xlist)):
    diff = ylist[i] - xlist[i]

    absresiduals.append(abs(diff))

## Squaring residuals- REMOVED PER DR STARDUST!
#for resid in residuals:
#	res_sq.append(resid**2)
	
	
sprmn_r, pval = (scipy.stats.mstats.spearmanr(xlist, ylist))
#rmse =  math.sqrt(sum(res_sq)/ (len(xlist)-1))
n = len(absresiduals)
mae = (sum(absresiduals))/ n
## adding txt to plots
plt.annotate("MAE = "+ str(round(mae,3)), xy = (6.5,0.5))
plt.annotate("n = " + str(n), xy = (7.125,3.5))
plt.annotate("r = " + str(round(sprmn_r, 3)), xy = (7.25, 2.5))
plt.annotate("p = " + str(round(float(pval),3)), xy = (7.125, 1.5))
#plt.annotate(s = "e", xy = (0.3,9), fontweight = 'bold')
plt.annotate(s = "j", xy = (0.3,9), fontweight = 'bold')

#plt.suptitle("Panel 'b'")
#plt.tight_layout()
plt.show()
treefile.close()

