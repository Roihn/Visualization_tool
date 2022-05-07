from config.colors import color
from src.load.load_bebold import load_csv_data_bebold

OUTPUT_DIR_NAME = "multiroom/"
OUTPUT_FILE_NAME = "multiroom_cbet_vssum_vsratio_{}"

TITLE = "multiroom_cbet_vssum_vsratio"

METRICS = ["episode_win", "episode_return"]
ENVS = ['N7-S4', 'N10-S4', 'N4-S5', 'N3-S6', 'N5-S6', 'N2-S8', 'N6-S8', 'N6-S10']

data_cbet = {"name": "cbet",
              "color": color[2],
              "dirs": ['/mnt/brain6/scratch/guoyijie/cbet/logs_minigrid_no_task/MiniGrid-MultiRoom-N7-S4-v0-cbet-s3-int0.005-no-reward/test_frame3000000_no_task',
                       '/mnt/brain6/scratch/guoyijie/cbet/logs_minigrid_no_task/MiniGrid-MultiRoom-N7-S4-v0-cbet-s4-int0.005-no-reward/test_frame3000000_no_task']
            }

data_vssum = {"name": "vssum",
              "color": color[3],
              "dirs": ['/mnt/brain6/scratch/guoyijie/cbet/logs_minigrid_no_task/MiniGrid-MultiRoom-N7-S4-v0-vssum-s4-int0.01-no-reward/test_frame1000000_no_task',
                       '/mnt/brain6/scratch/guoyijie/cbet/logs_minigrid_no_task/MiniGrid-MultiRoom-N7-S4-v0-vssum-s2-int0.01-no-reward/test_frame1000000_no_task']
             }

data_vsratio = {"name": "vsratio",
              "color": color[4],
              "dirs": ['/mnt/brain6/scratch/guoyijie/cbet/logs_minigrid_no_task/MiniGrid-MultiRoom-N7-S4-v0-vsratio-s3-int0.01-no-reward/test_frame1000000_no_task',
                       '/mnt/brain6/scratch/guoyijie/cbet/logs_minigrid_no_task/MiniGrid-MultiRoom-N7-S4-v0-vsratio-s2-int0.005-no-reward/test_frame2000000_no_task']
            }

DATA = [data_cbet, data_vssum, data_vsratio]

config = {
    "output_dir": OUTPUT_DIR_NAME,
    "output_file_name": OUTPUT_FILE_NAME,
    "data": DATA,
    "num_curves": len(DATA),
    "title": TITLE,
    "metrics": METRICS,
    "envs": ENVS,
}


