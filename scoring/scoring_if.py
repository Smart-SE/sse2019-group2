#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import subprocess

y_flg = True

def scoring(wav_filepath: str, beat: str, y_flg=True):
    if y_flg:
        o_score_consoleoutput = subprocess.check_output(
            ['Rscript', 'scoring_098.R', beat, wav_filepath], stderr=subprocess.DEVNULL)
        o_score = int(o_score_consoleoutput.split()[1])
        return o_score
    else:
    # 回避策用
        y_score = None
        try:
            y_score = y_module.predict_score(b=beat, file_path=wav_filepath)
        except:
            pass 
        if y_score is not None:
            # 平
            return y_score
        else:
            #ランダマイズ
            return y_score

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
