from src.pkg.pkg_default import *
from src.load.load_default import load_csv_data

def plot_curve(ax, x, y, color, label, linestyle, marker, 
               step=1, marker_size=4, linewidth=2, err_type='line'):
    
    mean = np.mean(y, axis=0)
    std = np.std(y, axis=0) / np.sqrt(y.shape[0])
    if err_type=='line':
        #maxes = []
        for i in range(y.shape[0]):
            #tmp = [e for e in y[i] if e >= 0]
            #ax.plot(x[:len(tmp)], tmp, color=color, label=None, marker=marker, 
            #        linestyle=linestyle, markersize=marker_size, alpha=0.3, linewidth=linewidth)
            #print('max', np.max(tmp))
            #maxes.append(np.max(tmp))
            ax.plot(x, y[i], color=color, label=None, marker=marker, 
                    linestyle=linestyle, markersize=marker_size, alpha=0.3, linewidth=linewidth)
        #print('average of max', np.mean(maxes))
    else:
        ax.fill_between(x, mean-std, mean+std, 
                        facecolor=color, interpolate=True, alpha=0.2, 
                        edgecolor='lightgrey', linewidth=0.5)
    
    ax.plot(x[:len(mean)], mean, color=color, label=label, marker=marker, 
            linestyle=linestyle, markersize=marker_size, alpha=1, linewidth=linewidth)
    
    return mean, std
    
def format_plot(ax, fig, max_size):
    #ax.set_xlabel('Step', fontsize=12)
    ax.relim()
    ax.autoscale_view()
    ax.set_xlim(0, max_size)
    ax.grid(which='both', alpha=0.6)
    ax.grid(which='both', alpha=0.6)    
    # ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels, loc=4, prop={'size':8}, labelspacing=0.01, borderpad=0.1)
    fig.tight_layout()

def plot_error(fig, ax, data, color, label, linestyle='-', marker='', 
               linewidth=2.5, max_step=60e6, interval=1e5, err_type='line',
               load_func=load_csv_data):
    step, vals = load_func(data, max_step=max_step, interval=interval)
    if step is None:
        return 0, 0
    mean, std = plot_curve(ax, step, vals, color, label, linestyle, marker, 
                           linewidth=linewidth, err_type=err_type)
    format_plot(ax, fig, max_step)
    return mean, std
        
def create_plot(width=10, height=8):    
    fig, ax = plt.subplots(1)
    fig.set_size_inches(width, height)
    return fig, ax

def plot(data, max_step=10e6):
    fig, ax = create_plot()
    
    for d in data:
        name = d['name']
        color = d['color']
        logdirs = d['logdirs']
        plot_error(fig, ax, logdirs, color, name, max_step=max_step)
    
    ax.set_ylabel('Average reward', fontsize=12)
    fig.savefig('plot/mujoco.png', bbox_inches='tight')
    fig.savefig('plot/mujoco.pdf', bbox_inches='tight')
    plt.close(fig)
    plt.close()
    display(Image(filename='plot/mujoco.png'))
    
def plot_multi(config, max_step=1e6, interval=1e4, err_type='line', 
               num_col=3, legend_idx=0, width=3.7, height=3, output_filename=None,
               x_label=None, y_label=None, title=None):
    num_plots = 1
    num_row = int((num_plots + num_col - 1)/num_col)
    fig, axes = plt.subplots(num_row, num_col)
    fig.set_size_inches(width*num_col, height*num_row)
    if not output_filename:
        output_filename = config["output_dir"] + config["output_file_name"]
    if not x_label:
        x_label = config["x_label"]
    if not y_label:
        y_label = config["y_label"]
    if not title:
        title = config["title"]
    
    for i, data in enumerate(config["data"]):
        # Each data represents one curve (model)
        if num_col > 1 or num_row > 1:
            ax = axes[int(i / num_col)][i % num_col] if num_row > 1 else axes[i]
        else:
            ax = axes
        name = data['name']
        color = data['color']
        logdirs = data['logdirs']
        load_func = data['load_func']
        mean, std = plot_error(fig, ax, logdirs, color, name, max_step=max_step, 
                                interval=interval, err_type=err_type, 
                                load_func=load_func)
            
        ax.set_xlim(0, max_step)
        #ax.set_xlabel('Million steps', fontsize=12)
        ax.set_title(title)
        ax.xaxis.set_ticks(np.arange(0, max_step+1, max_step/5))
        ticks = ticker.FuncFormatter(lambda x, pos: '{0:1.1f}M'.format(x/1000000.0))
        ax.xaxis.set_major_formatter(ticks)
        ax.legend().set_visible(False)
        ax.set_ylabel(y_label, fontsize=12)
        ax.set_xlabel(x_label, fontsize=12)
    
    for idx in range(num_plots+1, num_row*num_col):
        ax = axes[int(idx / num_col)][idx % num_col] if num_row > 1 else axes[idx]
        ax.set_axis_off()
            
    if num_row > 1 or num_col > 1:
        first_ax = axes[0][0] if num_row > 1 else axes[0]
        legend_ax = axes[int(legend_idx / num_col)][legend_idx % num_col] if num_row > 1 else axes[legend_idx]
    else:
        first_ax = axes
        if legend_idx > 0:
            legend_ax = axes
    if legend_idx == -1:
        legend_ax.set_axis_off()
    
    if legend_idx > 0:
        legend_ax.legend(*first_ax.get_legend_handles_labels(), loc = 'lower right', prop={'size':10})
    #    legend_ax.legend(*first_ax.get_legend_handles_labels(), loc = 'lower right')
    
    if "output_dir" in config.keys():
        os.makedirs("plot/" + config["output_dir"], exist_ok = True)
    fig.savefig('plot/%s.png' % output_filename, bbox_inches='tight', dpi=200)
    fig.savefig('plot/%s.pdf' % output_filename, bbox_inches='tight', dpi=200)
    plt.close(fig)
    plt.close()
    display(Image(filename='plot/%s.png' % output_filename))
