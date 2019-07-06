#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import subprocess

y_flg = True

def scoring(wav_filepath: str, beat: str, y_flg=True):
    o_score_consoleoutput = subprocess.check_output(
        ['Rscript', 'scoring_098.R', beat, wav_filepath], stderr=subprocess.DEVNULL)
    o_score = int(o_score_consoleoutput.split()[1])

    # 吉田は初めてで精度でないと思うので、切り離せるように
    if y_flg:
        # y_score = 50 #(吉田スコアリングモジュール実行)→暫定的に50を入れています =>Tureの時も値がちゃんと返るようにしました。
        y_score = None
        y_score = y_module.predict_score(b=beat, file_path=wav_filepath)
        # エラーハンドリング
        # ちゃんと値が返ったら平均、無いなら奥谷さんスコアそのまま返す
        if y_score is not None:
            # 平均処理
            ave_score = (o_score + y_score)/2
            return ave_score
        else:
            return o_score
    else:
        return o_score

# End


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-B')
    parser.add_argument('-f')
    args = parser.parse_args()

    beat = args.B
    wav_filepath = args.f

    y_flg = True
    score = scoring(wav_filepath, beat, y_flg)
    print(score)
