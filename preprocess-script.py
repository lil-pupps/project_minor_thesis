# import library
from __future__ import print_function

import argparse
import os
import shutil
import time
import random
from math import cos, pi
from sklearn.pipeline import Pipeline

parser = argparse.ArgumentParser(description='Pre Processing images')
# input images argument
parser.add_argument('-d', '--data', default='./data/',
                    type=str, help='path to dataset directory')


# TODO: add parser argument for:
# 1) dimensions (width,height) of output images
# 2) normalization and noise removal (need to research on how to apply it. Also, is there any library which could be used to speed up the process!)
# 3) smoothing and blurring


def main():
    args = parser.parse_args()
    # dummy pipeline, code to be replaced as the project progresses
    steps = [
        ('Read Images', get_images()),
        ('Resize images', image_resize())
    ]

    pipeline = Pipeline(steps)  # define the pipeline object.
