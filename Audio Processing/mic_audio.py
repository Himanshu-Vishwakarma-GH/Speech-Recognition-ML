import pyaudio  # Audio stream handle karne ke liye library import ki
import wave  # WAV file format handle karne ke liye library import ki

FRAMES_PER_BUFFER = 3200  # Ek buffer mein kitne frames honge define kiya
FORMAT = pyaudio.paInt16  # Audio format set kiya (16-bit audio)
CHANNELS = 1  # Mono audio ke liye channels set kiya
RATE = 16000  # Sampling rate set kiya (16 kHz)
p = pyaudio.PyAudio()  # PyAudio ka object banaya

# starts recording
stream = p.open(  # Audio stream open kiya
   format=FORMAT,  # Format set kiya
   channels=CHANNELS,  # Channels set kiya
   rate=RATE,  # Sampling rate set kiya
   input=True,  # Input mode enable kiya
   frames_per_buffer=FRAMES_PER_BUFFER  # Buffer size set kiya
)

print("start recording...")  # Recording start hone ka message print kiya

frames = []  # Audio frames store karne ke liye list banayi
seconds = 5  # Recording duration set kiya (5 seconds)
for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):  # Loop chalaya har buffer ke liye
    data = stream.read(FRAMES_PER_BUFFER)  # Buffer se audio data read kiya
    frames.append(data)  # Data ko frames list mein add kiya

print("recording stopped")  # Recording stop hone ka message print kiya

stream.stop_stream()  # Audio stream ko stop kiya
stream.close()  # Audio stream ko close kiya
p.terminate()  # PyAudio object ko terminate kiya

wf = wave.open("output.wav", 'wb')  # WAV file create ki write mode mein
wf.setnchannels(CHANNELS)  # File ke channels set kiye
wf.setsampwidth(p.get_sample_size(FORMAT))  # Sample width set kiya
wf.setframerate(RATE)  # Sampling rate set kiya
wf.writeframes(b''.join(frames))  # Frames ko WAV file mein write kiya
wf.close()  # WAV file ko close kiya