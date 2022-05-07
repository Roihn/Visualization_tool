from src.pkg.pkg_default import *
from src.load.load_default import load_pickles
    
def plot_barchart(config, metric:str = "episode_win"):
    bar_width = 0.2

    for i, info in enumerate(config["data"]):
        data = load_pickles(info["dirs"])
        # print(data)
        assert metric in data.keys()
        y = [np.mean(data[metric][key]) for key in config["envs"]]
        y_err = [np.std(data[metric][key]) for key in config["envs"]]
        x_base = np.arange(len(config["envs"]))
        x = [tmp + bar_width*i for tmp in x_base]
        name = info["name"]
        color = info["color"]
        plt.bar(x, y, width=bar_width, color=color, label=name, edgecolor='white')
        plt.errorbar(x, y, yerr=y_err, fmt=',', ecolor='lightgrey', elinewidth=1, capsize=2)

    y_label = metric
    x_ticks = config["envs"]

    output_filename = config["output_dir"] + config["output_file_name"].format(metric)
    title = config['title']
    
    # plt.ylim(0, 1)
    plt.title(title)
    plt.legend().set_visible(True)
    plt.ylabel(y_label, fontsize=12)
    plt.xticks(np.arange(len(x_ticks)) + bar_width * (len(config["data"])-1) / 2, x_ticks, fontsize=8)
  
    
    if "output_dir" in config.keys():
        os.makedirs("plot_barchart/" + config["output_dir"], exist_ok = True)
    plt.savefig('plot_barchart/%s.png' % output_filename, bbox_inches='tight', dpi=200)
    plt.savefig('plot_barchart/%s.pdf' % output_filename, bbox_inches='tight', dpi=200)
    plt.close()
    display(Image(filename='plot_barchart/%s.png' % output_filename))
