from pydub import AudioSegment

audio = AudioSegment.from_wav("Recording.wav")  # Load WAV file

# Increase volume by 6dB
audio = audio + 6
audio = audio * 2  # Double the volume

audio = audio.fade_in(2000)  # Apply a 2-second fade-in effect

audio.export("output.mp3", format="mp3")  # Export to MP3 format

audio2 = AudioSegment.from_mp3("output.mp3")  # Load MP3 file

print("Processing complete. Check 'output.mp3'")