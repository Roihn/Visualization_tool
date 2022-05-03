from config.colors import color
from src.load.load_bebold import load_csv_data_bebold
from src.load.load_cbet import load_csv_data_cbet

OUTPUT_DIR_NAME = "minigrid_multienv/"
OUTPUT_FILE_NAME = "minigrid_multienv_pre_trained_extrinsic_cbet"
X_LABEL = "Frame"
Y_LABEL = "Return"
TITLE = "minigrid_multienv_pre_trained_extrinsic_cbet"


data_cbet = {'name': r'cbet_official_pre_trained', 
                    'color': color[4],
                    'logdirs': ['/mnt/brain7/scratch/roihn/cbet/logs/cbet-20220422-200238/logs.csv',],
                    'load_func': load_csv_data_cbet,
                    'y_label': 'mean_rewards'
                }

DATA = [data_cbet] 

config = {
    "output_dir": OUTPUT_DIR_NAME,
    "output_file_name": OUTPUT_FILE_NAME,
    "data": DATA,
    "num_curves": len(DATA),
    "x_label": X_LABEL,
    "y_label": Y_LABEL,
    "title": TITLE,
}


