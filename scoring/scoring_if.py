#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import random
import os

#param
y_flg = True
#とりあえず/root下に置くと仮定
score_file_dir = "/root/smartSE/"

def scoring(wav_filepath: str, beat: str):
    if y_flg:
        o_score_consoleoutput = subprocess.check_output(
            ['Rscript', 'scoring_098.R', beat, wav_filepath], stderr=subprocess.DEVNULL)
        o_score = int(o_score_consoleoutput.split()[1])
        return o_score
    else:
        y_score = None
        try:
            if os.path.exists(os.path.join(score_file_dir, "s-100")) :
                y_score = random.randint(80, 100)
            elif os.path.exists(os.path.join(score_file_dir, "s-60")) :
                y_score = random.randint(50, 70)
            elif os.path.exists(os.path.join(score_file_dir, "s-20")) :
                y_score = random.randint(10, 30)
            else:
                raise FileNotFoundError
            #raise ValueError
            return y_score

        except FileNotFoundError:
            #debugの時切り分けようにFileNotFoundErrorはメッセージをprint
            print("score file not found")
            return random.randint(40, 70)
            pass
        except:
            return random.randint(40, 70)
            pass

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
