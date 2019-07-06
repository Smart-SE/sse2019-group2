#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import random

#param
y_flg = True



def scoring(wav_filepath: str, beat: str):
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
            return y_score
        else:
            #ランダマイズ
            return random.randint(0, 100)

# End


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-B')
    parser.add_argument('-f')
    args = parser.parse_args()

    beat = args.B
    wav_filepath = args.f

    score = scoring(wav_filepath, beat)
    print(score)
