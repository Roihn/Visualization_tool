from src.pkg.pkg_default import *
from src.load.load_default import csv_read

def load_csv_data_base(data, max_step=10**7, interval=10**6, 
                         step_label=,
                         reward_label=):
    # TODO: Modify default values of step_label and reward_label
    #       step_label is the column name of steps in your csv log file.
    #       reward_label is the column name of reward in your csv log file.
    x_max = max_step
    x_min = 0
    interpolation_func = []
    for x in data:
        steps = []
        vals = []
        df = csv_read(x)
        cur_steps = df[step_label].to_numpy()
        cur_vals = df[reward_label].to_numpy()

        cur_vals[np.isnan(cur_vals)] = 0 # 0 rewards are given as NaN for some reason..
        steps.extend(list(cur_steps))
        vals.extend(list(cur_vals))

        if len(vals)>0:
            tmp_vals = vals
            tmp_steps = steps
            interpolation_func.append(interpolate.interp1d(tmp_steps, tmp_vals))
            x_max = min(x_max, tmp_steps[-1])
            x_min = max(x_min, tmp_steps[0])
    if len(interpolation_func) == 0:
        return None, None
    stat_y = []
    stat_x = np.arange(x_min, x_max, interval)
    for f in interpolation_func:
        stat_y.append(f(stat_x))
        print('last step x', stat_x[-1])
        print('last step y', stat_y[-1][-1])
    rewards = [stat_y[i][-1] for i in range(len(stat_y))]
    print('average reward', np.mean(rewards), 'std', np.std(rewards)/np.sqrt(len(rewards)))
    return stat_x, np.stack(stat_y, axis=0)