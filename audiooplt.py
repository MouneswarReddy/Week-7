import soundfile as sf
from matplotlib import pyplot as plt
file_path="/home/smouneswar/Documents/week-7/aud.wav"
signal,sample_rate=sf.read(file_path)
duration=len(signal)/sample_rate
time=[i/sample_rate for i in range(len(signal))]
plt.figure(figsize=(10,4))
plt.plot(time,signal)
plt.title("audio signal")
plt.grid(True)
plt.show()
