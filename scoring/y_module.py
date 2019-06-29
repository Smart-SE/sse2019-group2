#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import sys
import traceback

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
