from config.colors import color
from src.load.load_bebold import load_csv_data_bebold
from src.load.load_cbet import load_csv_data_cbet

OUTPUT_DIR_NAME = "minigrid_n7s4/"
OUTPUT_FILE_NAME = "minigrid_n7s4_bebold_cbet"
X_LABEL = "Frame"
Y_LABEL = "Return"
TITLE = "minigrid_n7s4_bebold_cbet"


data_bebold = {'name': r'bebold_n7s4', 
                    'color': color[3],
                    'logdirs': ['/mnt/brain7/scratch/roihn/NovelD/experiments/MiniGrid-MultiRoom-N7-S4-v0-bebold-20220417-011751/logs.csv',],
                    'load_func': load_csv_data_bebold,
                   }


data_cbet = {'name': r'cbet_official_pre_trained', 
                    'color': color[4],
                    'logdirs': ['/mnt/brain7/scratch/roihn/cbet/logs/cbet-20220421-170817/logs.csv',],
                    'load_func': load_csv_data_cbet,
                   }

DATA = [data_bebold, data_cbet] 

config = {
    "output_dir": OUTPUT_DIR_NAME,
    "output_file_name": OUTPUT_FILE_NAME,
    "data": DATA,
    "num_curves": len(DATA),
    "x_label": X_LABEL,
    "y_label": Y_LABEL,
    "title": TITLE,
}


