import pydub
from pydub import AudioSegment
import os
import  numpy as np
import noisereduce as nr

audio = AudioSegment.from_file(r"C:\Users\hp\Downloads\Understanding This Python Calculator Code (Beginner Friendly) - Code Ghar.mp3")
srRate = audio.frame_rate
arraynums = audio.get_array_of_samples()

mydata = np.array(arraynums)

mysample = nr.reduce_noise(y=mydata, sr=srRate, stationary=False, prop_decrease=1.0)
clean_audio = audio._spawn(mysample.tobytes())
clean_audio.export(r"C:\Users\hp\Downloads\mysample.mp3",format="mp3")
print("done ")