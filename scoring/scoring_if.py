#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import y_module
import sys


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
if y_flg == True:
    #y_score = 50 #(吉田スコアリングモジュール実行)→暫定的に50を入れています =>Tureの時も値がちゃんと返るようにしました。
    y_score = None
    # y_score= y_module.predict_score(b= beat,filepath = wav_filepath)
    #エラーハンドリング
    #ちゃんと値が返ったら平均、無いなら奥谷さんスコアそのまま返す
    if y_score != None:
        #平均処理 切り捨て
        ave_score = int((o_score + y_score)/2)
        exit(ave_score)
    else:
        exit(o_score)
else:
    exit(o_score)

#End
