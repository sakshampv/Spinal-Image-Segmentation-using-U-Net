import numpy as np
import os
import pandas as pd
from PIL import Image


data_dir = "Training/"

def load_data(data_dir, directory, start, end):
    dataset = []
    for i in range(start, end):
        folder = "ID (" + str(i) + ")"
        curr_data = []
        try:
            #AP view
            curr_dir = data_dir + directory + folder + "/AP/"
            ap = Image.open(curr_dir+"AP.jpg").resize((2048, 1024))
            ap_pedicle = Image.open(curr_dir+"Ap_Pedicle.png").resize((2048, 1024))
            ap_spinous_process = Image.open(curr_dir+"Ap_Spinous_Process.png").resize((2048, 1024))
            ap_vertebra = Image.open(curr_dir+"Ap_Vertebra.png").resize((2048, 1024))

            #LAT view
            curr_dir = data_dir + directory + folder + "/LAT/"
            lat = Image.open(curr_dir+"LAT.jpg").resize((2048, 1024))
            lat_anterior_vertebral_line = Image.open(curr_dir+"Lat_Anterior_Vertebral_Line.png").resize((2048, 1024))
            lat_disk_height = Image.open(curr_dir+"Lat_Disk_Height.png").resize((2048, 1024))
            lat_posterior_vertebral_line = Image.open(curr_dir+"Lat_Posterior_Vertebral_Line.png").resize((2048, 1024))
            lat_spinous_process = Image.open(curr_dir+"Lat_Spinous_Process.png").resize((2048, 1024))
            lat_vertebra = Image.open(curr_dir+"Lat_Vertebra.png").resize((2048, 1024))

            curr_data = [i,ap, lat, ap_pedicle, ap_spinous_process, ap_vertebra, lat_anterior_vertebral_line, 
                         lat_disk_height, lat_posterior_vertebral_line, lat_spinous_process, lat_vertebra ]
            dataset.append(curr_data)
            
        except FileNotFoundError:
            print("Problem in folder: ", folder)
    return dataset



#load damaged data
print("Loading Damaged Data....")   
damaged_data = load_data(data_dir, "Damaged/", 1, 100)
#load normal data
print("Loading Normal Data....")
normal_data = load_data(data_dir, "Normal/", 1, 100)



damaged_df = pd.DataFrame(damaged_data)
normal_df = pd.DataFrame(normal_data)

column_names = ['ID', 'AP', 'LAT', 'AP_Pedicle', 'AP_Spinous_Process', "AP_Vertebreta", "LAT_Anterior_Vert_Line", 'LAT_disk_height', 'LAT_Posterior_Vert_Line', 'LAT_Spinal_Process', "LAT_Vertebra"]
damaged_df.columns = column_names
normal_df.columns = column_names

