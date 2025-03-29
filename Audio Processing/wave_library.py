# Auido Files Format : mp3(data compressed),flac(compressed but lossly),wav (uncompressed,highest quality)

import wave

# audio signal parameters
# sample_rate = 44100Hz #samples per second
# channels = 2 #stereo
# sample_width = 2 #bytes per sample (16 bits)
# width = 16 #bits per sample
# frames = 1024 #number of frames per buffer
# value = 0 #value of the sample

obj = wave.open("Recording.wav", "rb") 
#open the file in read binary mode -- get

print("Numbers of channels:",obj.getnchannels())
print("sample width:",obj.getsampwidth())
print("frame rate:",obj.getframerate())
print("number of frames:",obj.getnframes())
print("parameters:",obj.getparams())

timeaudio = obj.getnframes() / obj.getframerate()
print("Time Of Audio:",timeaudio,"sec")

frames = obj.readframes(-1) #read all the frames
print(type(frames), type(frames[0]))
print(len(frames))

obj.close()

"""--------------------------------------------------------------"""

newobj = wave.open("new_Recording.wav", "wb")
#open the file in write binary mode -- set

newobj.setnchannels(1)
newobj.setsampwidth(2)
newobj.setframerate(90000)
newobj.writeframes(frames) #write the frames to the file
newobj.close()
