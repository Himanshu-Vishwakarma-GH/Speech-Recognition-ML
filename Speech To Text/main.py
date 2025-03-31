import requests
from mainapp import *

filename = "Recording.wav"  # Audio file ka naam.
audio_url = upload(filename)

save_transcript(audio_url, 'file_title')