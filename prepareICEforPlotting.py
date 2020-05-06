#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:41:12 2020

@author: Jaakko Ahola, Finnish Meteorological Institute
@licence: MIT licence Copyright
"""
import time
import sys

sys.path.append('../LES-03plotting')
from Colorful import Colorful
from InputSimulation import InputSimulation

def prepareIceManuscriptData():

    colorDict ={
                "ICE0": Colorful.getDistinctColorList("green"),
                "ICE1": Colorful.getDistinctColorList("orange"),
                "ICE2": Colorful.getDistinctColorList("magenta"),
                "ICE3": Colorful.getDistinctColorList("teal"),
                "ICE4": Colorful.getDistinctColorList("blue"),
                "ICE5": Colorful.getDistinctColorList("maroon"),
                "ICE6": Colorful.getDistinctColorList("navy"),
                "BIN": Colorful.getDistinctColorList("black"),
                "BULK": Colorful.getDistinctColorList("grey"),
                "Prognostic": Colorful.getDistinctColorList("red"),
                "PrognosticAero": Colorful.getDistinctColorList("purple"),
                "Prognostic2": Colorful.getDistinctColorList("cyan"),
                "Prognostic2Aero": Colorful.getDistinctColorList("mint")}
                
    folder = "/home/aholaj/Nextcloud/kuvatesti/"
    
    manuscriptSimulationData = InputSimulation(
            idCollection = "ids.yaml",
            folderCollection="folders.yaml",
            labelCollection="labels.yaml",
            colorSet =  colorDict,
            folder = folder)
    
    manuscriptSimulationData.saveDataFrameAsCSV(folder, "manuscriptSimulationData.csv")

def main():
    prepareIceManuscriptData()
      
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Script completed in " + str(round((end - start),0)) + " seconds")
