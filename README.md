# Visualization Tool

By Run(Roihn) Peng

A lightweight, easy, extendable visualization tool for illustration.

# Tutorial

After several steps of implementation, you can easily generate your plottings with the following codes：

```python
from src.plot import plot_multi
# Only need to import one config file here
from config.experiments.minigrid_n6s10_bebold_cbet import config

# Only one line of code for plotting
plot_multi(config, err_type='area', max_step=20000000, interval=200000, num_col=1, width=4, height=3.5, legend_idx=1)
```

## CSV Loader

Each model / baseline has its own format of logs. To plot data from different models on one image, we need to construct specific loaders for each model we use.

For the simplest implementation, we only need to feed in the header name for the values of x-label and y-label as below:
```python
# src.load.load_base.py (Line 4)
def load_csv_data_base(data, max_step=10**7, interval=10**6, 
                         step_label=<x_label>,
                         reward_label=<y_label>)
```


We have provided you `src/load/load_base.py` as a start-up draft. It is recommended to copy and paste it under the path `src/load/`, so that you can easily find the loader for the model you use. 

## Config Generator

For every image you plot, it is highly recommended to record all of its information, so that you can easily check and revise it if needed. Here we also provide you `config/experiment_base.py` as a start-up draft. Yo can put it in the `config/experiments/` folder. In this config file, you need to import the loader you designed in the previous section, and put in other required information of your image.

After filling up all the required blanks, you can finally feed your config file into `src.plot.plot_multi()` to generate the plotting. Now let's go to `plot.ipynb` to check your work!

> You can also overwrite some of the arguments in `src.plot.plot_multi()` for quick access.




## Acknowledgements
The vanilla algorithm for visualization is based on Yijie Guo's code.