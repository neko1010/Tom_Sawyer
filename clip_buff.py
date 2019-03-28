#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nkolarik
#
# Created:     10/02/2018
# Copyright:   (c) nkolarik 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os
import shutil

def clipTrees(rootdir):
    """
    Clips tree locations to within ROI. Update ROI as necessary.
    Currently assumes data in 'stems' directory and an empty dir named 'clip' exists.
    """
    ENV = "C:\\Users\\nkolarik\\Desktop\\TomSawyer\\Tom_Sawyer_11Nov2017\\points2_ENV2.shp"
    cats = os.listdir(rootdir)
    for cat in cats:
        if cat.endswith('stems'):
            files = os.listdir(rootdir + cat)
            for file in files:
                if file.endswith("shp"):
                    arcpy.Clip_analysis(rootdir + cat + "\\" + file, ENV, rootdir + "clip\\" + file.split(".")[0] +"_clip.shp")
                    print (file + " Clipped")


def buffStems(rootdir):
    """
    Buffers stems based on estimated radii
    """
    cats = os.listdir(rootdir)
    for cat in cats:
        if cat == 'clip':
            for file in os.listdir(rootdir + cat):
                if file.endswith("clip.shp"):
                    arcpy.Buffer_analysis(rootdir + cat + "\\" + file, rootdir + cat + "\\" + file.split(".")[0] + "_buff", "Radius")
                    print ( file + " Buffed out")

def main():
    #rootdir = "enter directory here"
    clipTrees(rootdir)
    buffStems(rootdir)

if __name__ == '__main__':
    main()
