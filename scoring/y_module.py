#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import sys
import traceback
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
import os
import random
import pandas as pd
import librosa
import librosa.display
import re
#For Data Augumentation
from tensorflow.keras.preprocessing.image import ImageDataGenerator



def predict_score(b= 60 ,filepath = None)

    score = None

    try:
    
    
    except:
        print("ERROR")
        traceback.print_exc()   
        pass
    
    finally:
        return score


if __name__ == '__main__'

    parser = argparse.ArgumentParser()
    parser.add_argument('-B')   
    parser.add_argument('-f')
    args = parser.parse_args()
    beat = args.B
    wav_filepath = args.f

    return predict_score(b= beat,filepath = wav_filepath)

#End
