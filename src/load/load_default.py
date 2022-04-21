from src.pkg.pkg_default import *

def csv_read(file_name):
    try:
        return pd.read_csv(file_name)
    except ValueError as e:
        print(file_name)
        raise e

def get_ranges(folder_names):
    ranges = []
    start_step = 0
    for folder_name in folder_names[1:]:
        timestep = int(folder_name.split('_')[-1][:-1])*1e6
        ranges.append(timestep)
        start_step = timestep
    ranges.append(1000*1e6)
    return ranges

def load_csv_data(data, max_step=10**7, interval=10**6, y_name="episode_raw_reward",
                  file_name='progress.csv', multiply=1):
    data_valid = []
    for x in data:
        if os.path.isdir(x):
            data_valid.append(x)
        else:
            print(x + ' is not found.')
    
    idx = 0
    x_max = max_step
    x_min = 0
    interpolation_func = []
    for x in data_valid:
        print(y_name)
        folder_names = sorted(glob.glob(x+'_pretrain_*M')+[x])
        ranges = get_ranges(folder_names)
        steps = []
        vals = []
        for folder_name, cur_range in zip(folder_names, ranges):
            log_path = os.path.join(folder_name, file_name)
            print(log_path)
            log = csv_read(log_path)
            f = open(log_path, 'r')
            column_names = f.readline().replace('\n', '').split(',')
            if y_name not in column_names and y_name=='episode_raw_reward':
                y_name = 'eprew'
            if y_name not in column_names:
                break
            if y_name in column_names:
                reward_idx = column_names.index(y_name)
            if 'total_timesteps' not in column_names:
                step_idx = column_names.index("timesteps")
                #step_idx = column_names.index("update")
            else:
                step_idx = column_names.index("total_timesteps")
            if len(steps)>0:
                cur_steps = log[100:, step_idx]+steps[-1]
                cur_vals = log[100:, reward_idx]
            else:
                cur_steps = log[2:, step_idx]
                cur_vals = log[2:, reward_idx]
                if 'compute_timesteps' in column_names:
                    compute_step_idx = column_names.index('compute_timesteps')
                    cur_compute_steps = log[2:, compute_step_idx]
                    cur_go_steps = np.array(cur_steps) - np.array(cur_compute_steps)
                    cur_steps = cur_go_steps * multiply + np.array(cur_compute_steps)
                    cur_steps = list(cur_steps)
            cur_vals[np.isnan(cur_vals)] = 0 # 0 rewards are given as NaN for some reason..
            idxes = [i for i in range(len(cur_steps)) if cur_steps[i]>cur_range]
            if len(idxes) > 0:
                idx = idxes[0]
                steps.extend(list(cur_steps[:idx+1]))
                vals.extend(list(cur_vals[:idx+1]))
            else:
                steps.extend(list(cur_steps))
                vals.extend(list(cur_vals))
        if 'std_prior' in y_name or 'Std_Current' in y_name:
            vals = np.clip(vals, 0, 20)
        
        #if y_name=='reward':
        #    vals = np.clip(vals, 0, 1e6)
        if len(vals)>0:
            #tmp_vals = [vals[i] for i in range(len(vals)) if steps[i]<=x_max and steps[i]>10]
            #tmp_steps = [steps[i] for i in range(len(steps)) if steps[i]<=x_max and steps[i]>10]
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
