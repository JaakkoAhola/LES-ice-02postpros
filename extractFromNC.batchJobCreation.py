#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:25:32 2020

@author: Jaakko Ahola, Finnish Meteorological Institute
@licence: MIT licence Copyright
"""
import time
from pathlib import Path

def main():

    folder = Path("/home/aholaj/mounttauskansiot/puhtiwork/UCLALES-SALSA/BinnedData")
    for muuttuja in ["S_Naba", "S_Nabb","S_Ncba","S_Ncbb", "S_Niba","S_Nibb"]:
    
        string = f"""#!/bin/bash
#BATCH --job-name=Extract{muuttuja}
#SBATCH --account=project_2001927
#SBATCH --time=72:00:00
#SBATCH --mem-per-cpu=144G
#SBATCH --partition=fmi

module load nco

srun ncks -v {muuttuja} case_isdac_LVL5_3D_iceD_inter_48h.nc case_isdac_LVL5_3D_iceD_inter_48h_{muuttuja}.nc
"""
        print(string)
        text_file = open(folder / ("batchJobExtract_" + muuttuja + ".sh"), "w")
        text_file.write(string)
        text_file.close()



if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Script completed in " + str(round((end - start),0)) + " seconds")
