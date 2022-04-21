from config.colors import color

# import your specific load functions here for logs of different models
from src.load.load_base import load_csv_data_base


# output png / pdf file will be placed under plot/<OUTPUT_DIR_NAME>/<OUTPUT_FILE_NAME>.png/.pdf
OUTPUT_DIR_NAME = 
OUTPUT_FILE_NAME = 
# 
X_LABEL = "Frame"
Y_LABEL = "Return"
TITLE = 


data0 = {'name': r' ', 
                     'color': color[ ],
                     'logdirs': [' ',],
                     'load_func': load_csv_data_base,
                    }

data1 = {'name': r' ', 
                     'color': color[ ],
                     'logdirs': [' ',],
                     'load_func': load_csv_data_base,
                    }

DATA = [data0, data1, ]

config = {
    "output_dir": OUTPUT_DIR_NAME,
    "output_file_name": OUTPUT_FILE_NAME,
    "data": DATA,
    "num_curves": len(DATA),
    "x_label": X_LABEL,
    "y_label": Y_LABEL,
    "title": TITLE,
}


