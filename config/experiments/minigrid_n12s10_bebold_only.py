from config.colors import color
from src.load.load_bebold import load_csv_data_bebold
from src.load.load_cbet import load_csv_data_cbet

OUTPUT_DIR_NAME = "minigrid_n12s10/"
OUTPUT_FILE_NAME = "minigrid_n12s10_bebold_only"
X_LABEL = "Frame"
Y_LABEL = "Return"
TITLE = "minigrid_n12s10_bebold_only"


data_bebold = {'name': r'bebold_n7s4', 
                    'color': color[3],
                    'logdirs': ['/mnt/brain7/scratch/roihn/NovelD/experiments/MiniGrid-MultiRoom-N12-S10-v0-bebold-20220423-011033/logs.csv',],
                    'load_func': load_csv_data_bebold,
                   }



DATA = [data_bebold] 

config = {
    "output_dir": OUTPUT_DIR_NAME,
    "output_file_name": OUTPUT_FILE_NAME,
    "data": DATA,
    "num_curves": len(DATA),
    "x_label": X_LABEL,
    "y_label": Y_LABEL,
    "title": TITLE,
}


