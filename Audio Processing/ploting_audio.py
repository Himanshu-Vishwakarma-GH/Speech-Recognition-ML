import wave
import numpy as np
import matplotlib.pyplot as plt

# Audio file open kar
obj = wave.open("Recording.wav", "rb")

# Sample rate, total frames aur channels le
sample_fre = obj.getframerate()
n_sample = obj.getnframes()
n_channels = obj.getnchannels()  # Channels check karne ke liye

# Raw audio data read 
signal_wave = obj.readframes(-1)
obj.close()

# Total time calculate 
time_audio = n_sample / sample_fre
print(f"Audio Duration: {time_audio} seconds")

# Raw signal ko numpy array me convert 
signal_array = np.frombuffer(signal_wave, dtype=np.int16)

# Agar stereo hai to mono me convert 
if n_channels == 2:  
    signal_array = signal_array.reshape(-1, 2)  # 2 channels me reshape 
    signal_array = signal_array.mean(axis=1)  # Mean leke mono me convert 

# Time axis generate 
times = np.linspace(0, time_audio, num=len(signal_array))

# Plot create 
plt.figure(figsize=(15,6))
plt.plot(times, signal_array)
plt.title("Audio Signal Wave")
plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0, time_audio)
plt.show()



