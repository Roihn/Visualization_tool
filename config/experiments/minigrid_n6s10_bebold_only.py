from config.colors import color
from src.load.load_bebold import load_csv_data_bebold

OUTPUT_DIR_NAME = "minigrid_n6s10/"
OUTPUT_FILE_NAME = "minigrid_n6s10_bebold_only"
X_LABEL = "Episode"
Y_LABEL = "Reward"
TITLE = "minigrid_n6s10_bebold_only"


data_bebold_n6s10 = {'name': r'bebold_n6s10', 
                     'color': color[4],
                     'logdirs': ['/mnt/brain7/scratch/roihn/NovelD/experiments/MiniGrid-MultiRoom-N6-S10-v0-bebold-20220417-011737/logs.csv',],
                     'load_func': load_csv_data_bebold,
                    }
# data_bebold_n7s4 = {'name': r'bebold_n7s4', 
#                     'color': color[3],
#                     'logdirs': ['/mnt/brain7/scratch/roihn/NovelD/experiments/MiniGrid-MultiRoom-N7-S4-v0-bebold-20220417-011751/logs.csv',],
#                     'load_func': load_csv_data_bebold,
#                    }

DATA = [data_bebold_n6s10] #, data_bebold_n7s4]

config = {
    "output_dir": OUTPUT_DIR_NAME,
    "output_file_name": OUTPUT_FILE_NAME,
    "data": DATA,
    "num_curves": len(DATA),
    "x_label": X_LABEL,
    "y_label": Y_LABEL,
    "title": TITLE,
}


