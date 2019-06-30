import scoring_if
import audio

if __name__ == "__main__":
    audio.record()
    score = scoring_if.scoring('./output.wav', '100')
    print(score)
