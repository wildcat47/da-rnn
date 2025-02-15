import logging
import os

import matplotlib.pyplot as plt
import torch
from torch.autograd import Variable

from .constants import device


def setup_log(tag='VOC_TOPICS'):
    # create logger
    logger = logging.getLogger(tag)
    # logger.handlers = []
    logger.propagate = False
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    # logger.handlers = []
    logger.addHandler(ch)
    return logger


def save_or_show_plot(file_nm: str, save: bool):
    if save:
        plt.savefig(os.getcwd()+"/Figures/"+file_nm)
    else:
        plt.show()


def numpy_to_tvar(x):
    return Variable(torch.from_numpy(x).type(torch.FloatTensor).to(device))
