from config.colors import color
from src.load.load_bebold import load_csv_data_bebold
from src.load.load_cbet import load_csv_data_cbet

OUTPUT_DIR_NAME = "minigrid_n6s10/"
OUTPUT_FILE_NAME = "minigrid_n6s10_bebold_only"
X_LABEL = "Frame"
Y_LABEL = "Return"
TITLE = "minigrid_n6s10_bebold_cbet"


data_bebold = {'name': r'bebold', 
                     'color': color[4],
                     'logdirs': ['/mnt/brain7/scratch/roihn/NovelD/experiments/MiniGrid-MultiRoom-N6-S10-v0-bebold-20220417-011737/logs.csv',],
                     'load_func': load_csv_data_bebold,
                    }
data_cbet = {'name': r'cbet', 
                    'color': color[3],
                    'logdirs': ['/mnt/brain6/scratch/guoyijie/cbet/logs/MiniGrid-MultiRoom-N7-S4-v0-view-s0-e2-k1-int0.005/logs.csv',],
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


