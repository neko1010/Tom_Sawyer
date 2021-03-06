import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats

treefile = open("C:\\Users\\nkolarik\\Desktop\\TomSawyer\\output\\November\\ENVI_LiDAR\\field_trees.csv", 'r')
#treefile = open("C:\\Users\\nkolarik\\Desktop\\TomSawyer\\output\\July\\ENVI_LiDAR\\field_trees.csv", 'r')

tree_data = np.genfromtxt(treefile, delimiter = ",")

## coefficient of determination function ( r squared)
def rsquared(x,y):
	""" Returns R**2 where x and y are array-like objects"""
	slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x,y)
	return r_value**2, p_value

radii = [15, 18, 21, 24, 27]
subplots = [321, 322, 323, 324, 325]
colors = ["b", "g", "r", "magenta", "purple"]
titles = ["RGB", "Green", "Red", "Red Edge", "NIR"]
panels = ["(a)", "(b)", "(c)", "(d)", "(e)"]
#panels = ["(f)", "(g)", "(h)", "(i)", "(j)"]

for i in range(len(radii)):

	radius = radii[i]
	titles = ["RGB", "Green", "Red", "Red Edge", "NIR"]

	x = tree_data[1:, 12]
	y = tree_data[1:, radius]
	x1 = y1 = range(0,31)


	plt.subplot(subplots[i])
	plt.scatter(x,y, color = colors[i])
	plt.title(titles[i])
	plt.xlabel("Measured crown radius (m)")
	plt.ylabel("Estimated crown radius (m)")
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
	for j in range(0, len(xlist)):
		diff = ylist[j] - xlist[j]

		absresiduals.append(abs(diff))

	## Squaring residuals- REMOVED PER DR STARDUST!
	#for resid in residuals:
	#	res_sq.append(resid**2)
		
		
	#sprmn_r, pval = (scipy.stats.mstats.spearmanr(xlist, ylist))
	#rmse =  math.sqrt(sum(res_sq)/ (len(xlist)-1))

	## including r-squared for RSL reviewer
	r2, pval = rsquared(xlist,ylist)
	
	n = len(absresiduals)
	mae = (sum(absresiduals))/ n
	## adding txt to plots
	plt.annotate("MAE = "+ str(round(mae,2)), xy = (6.5, 0.5))
	plt.annotate("$n$ = " + str(n), xy = (7.125,3.5))
	#plt.annotate("r = " + str(round(sprmn_r, 3)), xy = (7.25, 2.5))
	plt.annotate("$R^2$ = " + str(round(r2, 2)), xy = (7, 2.5))
	plt.annotate("$p$ = " + str(round(float(pval),2)), xy = (7.125, 1.5))
	plt.annotate(s = panels[i], xy = (0.3,9), fontweight = 'bold')


plt.show()
treefile.close()

