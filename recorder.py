import sounddevice as sd
import wavio as wv
import datetime
import os

freq = 44100
duration = 5 # in seconds

os.makedirs(os.path.dirname('./recordings/'), exist_ok=True)
print('Recording')

while True:
    ts = datetime.datetime.now()
    filename = ts.strftime("%Y-%m-%d-%H-%M-%S")

    # Start recorder with the given values of duration and sample frequency
    # PTL Note: I had to change the channels value in the original code to fix a bug
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)

    # Record audio for the given number of seconds
    sd.wait()

    # Formatting and printing wav filename for saving
    wv_fname = "./recordings/" + filename + ".wav"
    print("saving",wv_fname)

    # Convert the NumPy array to audio file
    wv.write(wv_fname, recording, freq, sampwidth=2)