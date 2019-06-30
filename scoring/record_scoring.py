import csv
import datetime

import scoring_if
import audio

if __name__ == "__main__":
    formated_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    audio.record()
    score = scoring_if.scoring('./output.wav', '100')

    with open('/home/pi/sse2019-group2/outputs/result.csv', mode='a', newline='\n', encoding='utf-8') as fw:
        writer = csv.writer(fw)
        writer.writerow([formated_date, score])
