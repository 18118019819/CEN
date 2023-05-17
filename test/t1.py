import numpy as np

from rgcn import utils

data = utils.load_data("ICEWS14s")
train_list = utils.split_by_time(data.train)

