#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import subprocess


#parameter
y_flg = True


#main
parser = argparse.ArgumentParser()

parser.add_argument('-B')   
parser.add_argument('-f')
args = parser.parse_args()

beat = args.B
wav_filepath = args.f

o_score_consoleoutput = subprocess.check_output(['Rscript', 'scoring_098.R', beat, wav_filepath], stderr=subprocess.DEVNULL)
o_score = int(o_score_consoleoutput.split()[1])

#吉田は初めてで精度でないと思うので、切り離せるように
if y_flg = True:
    y_score = 50 #(吉田スコアリングモジュール実行)→暫定的に50を入れています

    #平均処理
    ave_score = (o_score + y_score)/2

    return ave_score

return o_score

#End


