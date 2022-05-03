from config.colors import color
from src.load.load_bebold import load_csv_data_bebold
from src.load.load_cbet import load_csv_data_cbet

OUTPUT_DIR_NAME = "minigrid_KeyCorridor/"
OUTPUT_FILE_NAME = "minigrid_KeyCorridor_bebold_only"
X_LABEL = "Frame"
Y_LABEL = "Return"
TITLE = "minigrid_KeyCorridor_bebold_only"


data_bebold_S5R3 = {'name': r'bebold_KeyCorridorS5R3', 
                    'color': color[3],
                    'logdirs': ['/mnt/brain7/scratch/roihn/NovelD/experiments/MiniGrid-KeyCorridorS5R3-v0-bebold-20220430-235855/logs.csv',],
                    'load_func': load_csv_data_bebold,
                   }

# data_bebold_2Q = {'name': r'bebold_ObstructedMaze_2Q', 
#                     'color': color[4],
#                     'logdirs': ['/mnt/brain7/scratch/roihn/NovelD/experiments/MiniGrid-ObstructedMaze-2Q-v0-bebold-20220428-032111/logs.csv',],
#                     'load_func': load_csv_data_bebold,
#                    }


DATA = [data_bebold_S5R3] 

config = {
    "output_dir": OUTPUT_DIR_NAME,
    "output_file_name": OUTPUT_FILE_NAME,
    "data": DATA,
    "num_curves": len(DATA),
    "x_label": X_LABEL,
    "y_label": Y_LABEL,
    "title": TITLE,
}


