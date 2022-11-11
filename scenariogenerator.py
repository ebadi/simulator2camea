import os, glob
import time
import requests
import matplotlib.pyplot as plt
import cv2

from subprocess import check_output
import shutil
import json
import mutate
import sys

# add cwd variable as the first parameter of join if it is necessary
cwd = os.getcwd()
scenarioCount= int(sys.argv[1])
for i in range(1,scenarioCount+1):
    print("running scenario: ", i,  "/", scenarioCount )
    ######## STEP 1 : Modify the json scenario file ########
    with open(os.path.join(cwd, "scenario.JSON"), 'r') as f:
        data = json.load(f)
        data['id'] = 134 # <--- add `id` value.

    new_data = mutate.data_mutate(data)

    with open(os.path.join(cwd, "scenario_modified.JSON"), 'w') as f:
        json.dump(new_data, f, indent=4)


    ######## STEP 2 : Run the json scenario file ########


    # path = os.path.join("LP_DATASET", "CAMEA")
    # path = os.path.join("LP_DATASET","INFOTIV", "png")
    path = os.path.join("LP_DATASET", "BERGE", "Normal")
    # try: 
    #     shutil.rmtree(path)
    # except:
    #     pass

    check_output(".\\Deccq_V3.0.0.1\\Deccq.exe -scenario=\"" + os.path.join(cwd, "scenario_modified.JSON") + "\"", shell=True)

