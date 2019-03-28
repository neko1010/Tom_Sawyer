#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nkolarik
#
# Created:     07/02/2018
# Copyright:   (c) nkolarik 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os

#rootdir = "enter directory here"
cats = os.listdir(rootdir)

for cat in cats:
    for file in os.listdir(rootdir + cat):
        if file.endswith("clip.shp"):
            arcpy.Buffer_analysis(rootdir + cat + "\\" + file, rootdir + cat + "\\" + cat + "_buff\\" + file.split(".")[0] + "_buff", "Radius")
            print ( file + " Buffed out")

def main():
    pass

if __name__ == '__main__':
    main()
