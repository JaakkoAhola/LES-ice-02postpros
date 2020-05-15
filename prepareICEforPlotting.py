#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:41:12 2020

@author: Jaakko Ahola, Finnish Meteorological Institute
@licence: MIT licence Copyright
"""
import numpy
import os
import sys
import time
import pathlib


sys.path.append('../LES-03plotting')
from Colorful import Colorful
from InputSimulation import InputSimulation

def prepareIceManuscriptData(simulationFolderIDLabel):
    
    # set environment variable ${SIMULATIONDATAROOTFOLDER} with 
    # folder that you have stored all the individual simulation folder
    simulationDataRootFolder = pathlib.Path(os.environ["SIMULATIONDATAROOTFOLDER"])
    
    simulationFolderIDLabel = numpy.asarray(simulationFolderIDLabel)
    
    folderList = [ simulationDataRootFolder / folder  for folder in simulationFolderIDLabel[:,0] ]
    IDList = [ ID for ID in simulationFolderIDLabel[:,1] ]
    labelList = [ label for label in simulationFolderIDLabel[:,2] ]

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
                "Prognostic": Colorful.getDistinctColorList("red")}
                
    # set environment variable ${SIMULATIONFIGUREFOLDER} with the folder that you want to store your figures
    figureFolder = os.environ["SIMULATIONFIGUREFOLDER"]
    
    manuscriptSimulationData = InputSimulation(
            idCollection = IDList,
            folderCollection = folderList,
            labelCollection = labelList,
            colorSet =  colorDict)
    
    manuscriptSimulationData.saveDataFrameAsCSV(figureFolder, "manuscriptSimulationData.csv")

def main():
    
    # simulationFolder, ID, LABEL
    simulationFolderIDLabel = [['case_isdac_LVL5_3D_iceD_0_8h','ICE0_8h', 'ICE0'],
       ['case_isdac_LVL5_3D_iceD_1_24h','ICE1_24h', 'ICE1'],
       ['case_isdac_LVL5_3D_iceD_1_8h','ICE1_8h', 'ICE1'],
       ['case_isdac_LVL5_3D_iceD_2_24h','ICE2_24h', 'ICE2'],
       ['case_isdac_LVL5_3D_iceD_2_8h','ICE2_8h', 'ICE2'],
       ['case_isdac_LVL5_3D_iceD_3_24h', 'ICE3_24h', 'ICE3'],
       ['case_isdac_LVL5_3D_iceD_3_8h', 'ICE3_8h', 'ICE3'],
       ['case_isdac_LVL5_3D_iceD_4_24h', 'ICE4_24h', 'ICE4'],
       ['case_isdac_LVL5_3D_iceD_4_8h', 'ICE4_8h', 'ICE4'],
       ['case_isdac_LVL5_3D_iceD_5_8h', 'ICE5_8h', 'ICE5'],
       ['case_isdac_LVL5_3D_iceD_6_8h', 'ICE6_8h', 'ICE6'],
       ['case_isdac_LVL5_3D_iceD_inter_48h', 'Prognostic_48h', 'Prognostic'],
       ['case_isdac_Ovchinnikov_COSMO_ice0', 'COSMO_ice0', 'BULK'],
       ['case_isdac_Ovchinnikov_COSMO_ice1', 'COSMO_ice1', 'BULK'],
       ['case_isdac_Ovchinnikov_COSMO_ice4', 'COSMO_ice4', 'BULK'],
       ['case_isdac_Ovchinnikov_DHARMA-2M_ice0', 'DHARMA-2M_ice0', 'BULK'],
       ['case_isdac_Ovchinnikov_DHARMA-2M_ice1', 'DHARMA-2M_ice1', 'BULK'],
       ['case_isdac_Ovchinnikov_DHARMA-2M_ice4', 'DHARMA-2M_ice4', 'BULK'],
       ['case_isdac_Ovchinnikov_DHARMA-bin_ice0', 'DHARMA-bin_ice0', 'BIN'],
       ['case_isdac_Ovchinnikov_DHARMA-bin_ice1', 'DHARMA-bin_ice1', 'BIN'],
       ['case_isdac_Ovchinnikov_DHARMA-bin_ice4', 'DHARMA-bin_ice4', 'BIN'],
       ['case_isdac_Ovchinnikov_METO_ice0', 'METO_ice0', 'BULK'],
       ['case_isdac_Ovchinnikov_METO_ice1', 'METO_ice1', 'BULK'],
       ['case_isdac_Ovchinnikov_METO_ice4', 'METO_ice4', 'BULK'],
       ['case_isdac_Ovchinnikov_RAMS_ice0', 'RAMS_ice0', 'BULK'],
       ['case_isdac_Ovchinnikov_RAMS_ice1', 'RAMS_ice1', 'BULK'],
       ['case_isdac_Ovchinnikov_RAMS_ice4', 'RAMS_ice4', 'BULK'],
       ['case_isdac_Ovchinnikov_SAM-2M_ice0', 'SAM-2M_ice0', 'BULK'],
       ['case_isdac_Ovchinnikov_SAM-2M_ice1', 'SAM-2M_ice1', 'BULK'],
       ['case_isdac_Ovchinnikov_SAM-2M_ice4', 'SAM-2M_ice4', 'BULK'],
       ['case_isdac_Ovchinnikov_SAM-bin_ice0', 'SAM-bin_ice0', 'BIN'],
       ['case_isdac_Ovchinnikov_SAM-bin_ice1', 'SAM-bin_ice1', 'BIN'],
       ['case_isdac_Ovchinnikov_SAM-bin_ice4', 'SAM-bin_ice4', 'BIN'],
       ['case_isdac_Ovchinnikov_UCLALES_ice0', 'UCLALES_ice0', 'BULK'],
       ['case_isdac_Ovchinnikov_UCLALES_ice1', 'UCLALES_ice1', 'BULK'],
       ['case_isdac_Ovchinnikov_UCLALES_ice4', 'UCLALES_ice4', 'BULK'],
       ['case_isdac_Ovchinnikov_UCLALES-SB_ice0', 'UCLALES-SB_ice0', 'BULK'],
       ['case_isdac_Ovchinnikov_UCLALES-SB_ice1', 'UCLALES-SB_ice1', 'BULK'],
       ['case_isdac_Ovchinnikov_UCLALES-SB_ice4', 'UCLALES-SB_ice4', 'BULK'],
       ['case_isdac_Ovchinnikov_WRFLES_ice0', 'WRFLES_ice0', 'BULK'],
       ['case_isdac_Ovchinnikov_WRFLES_ice1', 'WRFLES_ice1', 'BULK'],
       ['case_isdac_Ovchinnikov_WRFLES_ice4', 'WRFLES_ice4', 'BULK'],
       ['case_isdac_Ovchinnikov_WRFLES-PSU_ice0', 'WRFLES-PSU_ice0', 'BULK'],
       ['case_isdac_Ovchinnikov_WRFLES-PSU_ice1', 'WRFLES-PSU_ice1', 'BULK'],
       ['case_isdac_Ovchinnikov_WRFLES-PSU_ice4','WRFLES-PSU_ice4', 'BULK']]
    
    
    prepareIceManuscriptData(simulationFolderIDLabel)
      
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Script completed in " + str(round((end - start),0)) + " seconds")
