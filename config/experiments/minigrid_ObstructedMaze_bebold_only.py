from config.colors import color
from src.load.load_bebold import load_csv_data_bebold
from src.load.load_cbet import load_csv_data_cbet

OUTPUT_DIR_NAME = "minigrid_ObstructedMaze/"
OUTPUT_FILE_NAME = "minigrid_ObstructedMaze_bebold_only"
X_LABEL = "Frame"
Y_LABEL = "Return"
TITLE = "minigrid_ObstructedMaze_bebold_only"


data_bebold_1Q = {'name': r'bebold_ObstructedMaze_1Q', 
                    'color': color[3],
                    'logdirs': ['/mnt/brain7/scratch/roihn/NovelD/experiments/MiniGrid-ObstructedMaze-1Q-v0-bebold-20220428-161006/logs.csv',],
                    'load_func': load_csv_data_bebold,
                   }

data_bebold_2Dlh = {'name': r'bebold_ObstructedMaze_2Dlh', 
                    'color': color[4],
                    'logdirs': ['/mnt/brain7/scratch/roihn/NovelD/experiments/MiniGrid-ObstructedMaze-2Dlh-v0-bebold-20220502-025210/logs.csv',],
                    'load_func': load_csv_data_bebold,
                   }


DATA = [data_bebold_1Q, data_bebold_2Dlh] 

config = {
    "output_dir": OUTPUT_DIR_NAME,
    "output_file_name": OUTPUT_FILE_NAME,
    "data": DATA,
    "num_curves": len(DATA),
    "x_label": X_LABEL,
    "y_label": Y_LABEL,
    "title": TITLE,
}


