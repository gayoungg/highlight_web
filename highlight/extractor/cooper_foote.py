import numpy as np
import librosa
import glob
from highlight.extractor.ssm import ssm
from openpyxl import Workbook

class audio_thumb_cf:
    def __init__(self, audio_path, t = 'chroma', k = 10, smooth = 1, thresh = 1):
        self.ssm = ssm(audio_path, k, t, smooth, thresh)
        # print("New ssm", self.ssm.s)
        self.y, self.sr  = librosa.load(audio_path)
        self.time = 0

    def score_normalized(self, q, r):
        return np.sum(np.sum(self.ssm.s[:,q : r + 1], axis = 0)/(self.ssm.s.shape[0]*(r - q + 1)))

    def score_Q(self, L, i):
        return self.score_normalized(i, i + L - 1)

    def score_max(self, L):
        N = self.ssm.s.shape[0]
        s = np.array([])

        for i in range(N - L + 1):
            s = np.append(s, self.score_Q(L, i))
        return s.argmax()

    def thumb_alpha(self, L):
        q_max = self.score_max(L)
#        self.thumb_frame = q_max
        print("highlight with length " + str(round(self.frame_to_time(L), 2)) + " starts at time: " + str(round(self.frame_to_time(q_max), 2)) + "s")

    def thumb_time(self, time):
        L = self.time_to_frame(time)
        q_max = self.score_max(L)
        self.time = self.frame_to_time(q_max)
        print("highlight with length " + str(round(self.frame_to_time(L), 2)) + " starts at time: " + str(round(self.frame_to_time(q_max), 2)) + "s")
        return int(self.frame_to_time(q_max));

    def frame_to_time(self, f):
        dt = self.ssm.duration/self.ssm.s.shape[0]
        return dt*f

    def time_to_frame(self, time):
        df = self.ssm.s.shape[0]/self.ssm.duration
        return int(df*time)

    '''
    def display(self):
        if self.time == 0:
            print("run thumb_time() or thumb_alpha()")
        else:
            frame = int(len(self.y)*self.time_to_frame(self.time)/self.ssm.duration)
            IPython.display.Audio(data = self.y[frame:], rate = self.sr)

    '''
def all():
    fs = sorted(glob.glob('../../music/input.mp3'))
    wb = Workbook()
    ws = wb.active

    for f in fs:
        name = f.split('/')[-1][:-4]
        print(name, 'processing...')
        at=audio_thumb_cf(f)
        index=at.thumb_time(30)
        highlight=[index, index+30]
        print("Saving highlight...")
        print(highlight[0], " ", highlight[1])
        librosa.output.write_wav('./output/{}.wav'.format(name+"new"), at.y[highlight[0]*22050:highlight[1]*22050], 22050)
        ws.append([name, highlight[0], highlight[1]])
        wb.save('output.xlsx')
