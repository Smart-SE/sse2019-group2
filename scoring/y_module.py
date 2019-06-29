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

#param define
kijun = 60
sr_ef = 200
width = 46


def load_wave_data(file_name):
    file_path = os.path.join(WAV_DIR, file_name) #推論時はファイルパスまんま渡されるはず。
    shs, fs = librosa.load(file_path, sr=samling_rate)
    return shs,fs


def calculate_melsp(x, n_fft=2048, hop_length=128):
    stft = np.abs(librosa.stft(x, n_fft=n_fft, hop_length=hop_length))**2
    log_stft = librosa.power_to_db(stft)
    melsp = librosa.feature.melspectrogram(S=log_stft,n_mels=128)
    return melsp

def min_max(x, axis=None):
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    result = (x-min)/(max-min)
    return result

def predict_score(b= 120 ,filepath = None)
    score = None

    samling_rate =  int(sr_ef *(tenpo/kijun))
    
    
    X_pred = []
    
    try:
        shs, fs = load_wave_data("100_flog_01.wav")
        melsp = calculate_melsp(shs)
        # 注意　
        if melsp.shape[1] > width:
            melsp_new = melsp[:,0:width]
        else:
            melsp_new = melsp 
   
        melsp_reg_ndary = min_max(melsp_new)
        melsp_reg_ndary_reshape = np.expand_dims(melsp_reg_ndary, axis=-1)
       
        X_pred.append(melsp_reg_ndary_reshape)
    
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
