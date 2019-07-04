#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import traceback
import argparse

import numpy as np
import pickle
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
import librosa

#param define
kijun = 100
width = 800
#modelfilepath = "/root/smartSE/y_model.pickle"
modelfilepath = "./y_model.pickle"
henkou_score = None


def load_wave_data(file_path):
    music, fs = librosa.load(file_path)
    return music,fs

def min_max(x, axis=None):
    min = x.min(axis=axis, keepdims=True)
    max = x.max(axis=axis, keepdims=True)
    result = (x-min)/(max-min)
    return result

def rangecontrol(i):
    #print(i)
    if i > 100 :
        ten = 100 - (i - 100)
        return int(ten)
    elif i < 0 :
        ten = 0 + (-1 * i)
        return int(ten)
    else:
      return int(i)

def predict_score(b = 100 ,file_path = None):
    henkou_score = None
    X_pred = []   
    
    try:
        #model load
        with open(modelfilepath, 'rb') as f:
            model = pickle.load(f)

        # preparation
        music, fs = load_wave_data(file_path)
        CQ_spectro = np.abs(librosa.cqt(y=music, sr=fs, bins_per_octave=12*3, n_bins=7*12*3))
        # width is magic number
        if CQ_spectro.shape[1] > width:
            CQ_spectro_new = CQ_spectro[:,0:width]
        else:
            CQ_spectro_new = CQ_spectro 

        CQ_spectro_reg_ndary  =min_max(CQ_spectro_new)
        CQ_spectro_ndary_reshape = np.expand_dims(CQ_spectro_reg_ndary, axis=-1)
        X_pred.append(CQ_spectro_ndary_reshape)
        X_pred_npary = np.array(X_pred)        
        # predict
        pred= model.predict(X_pred_npary)
        henkou_score = rangecontrol(pred[0])
        return henkou_score
    except:
        print("ERROR")
        traceback.print_exc()   
        pass
    
    finally:
        return henkou_score


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-B')   
    parser.add_argument('-f')
    args = parser.parse_args()
    beat = args.B
    wav_filepath = args.f
    y_score = predict_score(b= beat, file_path = wav_filepath)
    exit(y_score)
#End
