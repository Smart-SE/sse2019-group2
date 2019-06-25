#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse


#parameter
y_flg = True


#main
parser = argparse.ArgumentParser()

parser.add_argument('-B')   
parser.add_argument('-f')
args = parser.parse_args()

beat = args.B
wav_filepath = args.f


#奥谷さんスコアリングモジュール実行箇所


#吉田は初めてで精度でないと思うので、切り離せるように
if y_flg = True:
    y_score = (吉田スコアリングモジュール実行)

    #平均処理
    ave_score = ({奥谷さんスコア} + y_score)/2

    return ave_score

return {奥谷さんスコア}

#End


