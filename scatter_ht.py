
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats

treefile = open("C:\\Users\\nkolarik\\Desktop\\TomSawyer\\output\\November\\ENVI_LiDAR\\field_trees.csv", 'r')
#treefile = open("C:\\Users\\nkolarik\\Desktop\\TomSawyer\\output\\July\\ENVI_LiDAR\\field_trees.csv", 'r')
## figure out how to 'vlookup' by ORIG_FID?
##Cheated- put all data into one table...
## pandas merge?
tree_data = np.genfromtxt(treefile, delimiter = ",")


##establishing heights (column of data file)
height = 14
titles = ["RGB", "Green", "Red", "Red Edge", "NIR"]

x = tree_data[1:, 11]
y = tree_data[1:, height]
x1 = y1 = range(0,31)

##subplots (# of rows, # of columns, 1 - (rows * columns))
plt.subplot(321)
plt.scatter(x,y)#, '+')
plt.title(titles[0])
plt.xlabel("Field Measurement")
plt.ylabel("Estimate")
plt.axis([0,30,0,30])
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
plt.annotate("MAE = "+ str(round(mae,3)), xy = (18, 2))
plt.annotate("n = " + str(n), xy = (21, 14))
plt.annotate("r = " + str(round(sprmn_r, 3)), xy = (21.25, 10))
plt.annotate("p = " + str(round(float(pval),3)), xy = (21, 6))
plt.annotate(s = "a", xy = (1,26), fontweight = 'bold')
#plt.annotate(s = "f", xy = (1,26), fontweight = 'bold')


height = 17
y = tree_data[1:, height]
plt.subplot(322)
plt.scatter(x,y, color = 'g')
plt.title(titles[1])
plt.xlabel("Field Measurement")
plt.ylabel("Estimate")
plt.axis([0,30,0,30])
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
plt.annotate("MAE = "+ str(round(mae,3)), xy = (18, 2))
plt.annotate("n = " + str(n), xy = (21, 14))
plt.annotate("r = " + str(round(sprmn_r, 3)), xy = (21.25, 10))
plt.annotate("p = " + str(round(float(pval),3)), xy = (21, 6))
plt.annotate(s = "b", xy = (1,26), fontweight = 'bold')
#plt.annotate(s = "g", xy = (1,26), fontweight = 'bold')

height = 20
y = tree_data[1:, height]
plt.subplot(323)
plt.scatter(x,y, color = 'r')
plt.title(titles[2])
plt.xlabel("Field Measurement")
plt.ylabel("Estimate")
plt.axis([0,30,0,30])
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
plt.annotate("MAE = "+ str(round(mae,3)), xy = (18, 2))
plt.annotate("n = " + str(n), xy = (21, 14))
plt.annotate("r = " + str(round(sprmn_r, 3)), xy = (21.25, 10))
plt.annotate("p = " + str(round(float(pval),3)), xy = (21, 6))
plt.annotate(s = "c", xy = (1,26), fontweight = 'bold')
#plt.annotate(s = "h", xy = (1,26), fontweight = 'bold')

height = 23
y = tree_data[1:, height]
plt.subplot(324)
plt.scatter(x,y, color = 'magenta')
plt.title(titles[3])
plt.xlabel("Field Measurement")
plt.ylabel("Estimate")
plt.axis([0,30,0,30])
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
plt.annotate("MAE = "+ str(round(mae,3)), xy = (18, 2))
plt.annotate("n = " + str(n), xy = (21, 14))
plt.annotate("r = " + str(round(sprmn_r, 3)), xy = (21.25, 10))
plt.annotate("p = " + str(round(float(pval),3)), xy = (21, 6))
plt.annotate(s = "d", xy = (1,26), fontweight = 'bold')
#plt.annotate(s = "i", xy = (1,26), fontweight = 'bold')

height = 26
y = tree_data[1:, height]
plt.subplot(325)
plt.scatter(x,y, color = 'purple')
plt.title(titles[4])
plt.xlabel("Field Measurement")
plt.ylabel("Estimate")
plt.axis([0,30,0,30])
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
plt.annotate("MAE = "+ str(round(mae,3)), xy = (18, 2))
plt.annotate("n = " + str(n), xy = (21, 14))
plt.annotate("r = " + str(round(sprmn_r, 3)), xy = (21.25, 10))
plt.annotate("p = " + str(round(float(pval),3)), xy = (21, 6))
plt.annotate(s = "e", xy = (1,26), fontweight = 'bold')
#plt.annotate(s = "j", xy = (1,26), fontweight = 'bold')


#plt.suptitle("Panel 'a'")
#plt.tight_layout()
plt.show()
treefile.close()
