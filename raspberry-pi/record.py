##人感センサースタートでRaspberry Piが録音を開始（5秒）

#coding: utf-8

import wiringpi as pi
import time
import pyaudio
import wave
import os
import requests
from datetime import datetime

PIR_PIN = 18
pi.wiringPiSetupGpio()
pi.pinMode(PIR_PIN, pi.INPUT)

count = 0
while True:
  if (pi.digitalRead(PIR_PIN) == pi.HIGH):
    if count > 20:
        print("A person was detected.")
        CHUNK = 1024*4
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        RECORD_SECONDS = 10
        WAVE_OUTPUT_FILENAME = datetime.now().strftime('%Y%m%d-%H%M%S') + "output.wav"
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
        print("* recording")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("* done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
#uplodad to slack

        TOKEN = ‘xoxp-●●●●’ /* slackから発行されたtoken */
        CHANNEL = ‘●●●●●’ /* slack channel  */
        TITLE = WAVE_OUTPUT_FILENAME
        files = {'file': open(WAVE_OUTPUT_FILENAME, 'rb')}
        param = {
            'token':TOKEN,
            'channels':CHANNEL,
            'filename':WAVE_OUTPUT_FILENAME,
            'initial_comment': "今日も練習お疲れさまでした！",'title': TITLE
            }
        requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
        
        time.sleep(3)
        count=0
    count= count+1
    print(count)
    time.sleep(0.1)
    
  else:
    count = 0
    time.sleep(0.5)
