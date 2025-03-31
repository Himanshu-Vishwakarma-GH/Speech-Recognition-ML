import requests  # HTTP requests ke liye import
import json  # JSON data handle karne ke liye import
import time  # Time delay ke liye import
from api_secrets import API_KEY_ASSEMBLYAI  # API key import karo

upload_endpoint = 'https://api.assemblyai.com/v2/upload'  # Upload endpoint ka URL
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'  # Transcript endpoint ka URL

headers_auth_only = {'authorization': API_KEY_ASSEMBLYAI}  # Sirf authorization ke liye headers

headers = {  # Authorization aur content type ke liye headers
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}

CHUNK_SIZE = 5_242_880  # File upload ke liye chunk size (5MB)

# File ko upload karne ka function
def upload(filename):
    def read_file(filename):  # File ko chunk me read karne ka generator
        with open(filename, 'rb') as f:
            while True:
                data = f.read(CHUNK_SIZE)  # Chunk size ke hisaab se data read karo
                if not data:  # Agar data khatam ho gaya
                    break
                yield data

    upload_response = requests.post(upload_endpoint, headers=headers_auth_only, data=read_file(filename))  # File upload karo
    return upload_response.json()['upload_url']  # Upload URL return karo

# Audio ko transcribe karne ka function
def transcribe(audio_url, sentiment_analysis):
    transcript_request = {  # Request body prepare karo
        'audio_url': audio_url,
        'sentiment_analysis': sentiment_analysis
    }

    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)  # Transcript request bhejo
    return transcript_response.json()['id']  # Transcript ID return karo

# Transcript status ko poll karne ka function
def poll(transcript_id):
    polling_endpoint = transcript_endpoint + '/' + transcript_id  # Polling endpoint ka URL
    polling_response = requests.get(polling_endpoint, headers=headers)  # Polling request bhejo
    return polling_response.json()  # Response return karo

# Transcript result aur error ko fetch karne ka function
def get_transcription_result_url(url, sentiment_analysis):
    transcribe_id = transcribe(url, sentiment_analysis)  # Transcribe ID le lo
    while True:
        data = poll(transcribe_id)  # Poll karo
        if data['status'] == 'completed':  # Agar status completed hai
            return data, None  # Data return karo
        elif data['status'] == 'error':  # Agar error hai
            return data, data['error']  # Error return karo
            
        print("waiting for 30 seconds")  # Wait message print karo
        time.sleep(30)  # 30 seconds ka delay

# Transcript ko save karne ka function
def save_transcript(url, title, sentiment_analysis=False):
    data, error = get_transcription_result_url(url, sentiment_analysis)  # Transcript result fetch karo
    
    if data:  # Agar data mila
        filename = title + '.txt'  # Text file ka naam banao
        with open(filename, 'w') as f:  # File ko write mode me open karo
            f.write(data['text'])  # Text save karo
             
        if sentiment_analysis:  # Agar sentiment analysis enable hai
            filename = title + '_sentiments.json'  # JSON file ka naam banao
            with open(filename, 'w') as f:  # File ko write mode me open karo
                sentiments = data['sentiment_analysis_results']  # Sentiments extract karo
                json.dump(sentiments, f, indent=4)  # JSON file me save karo
        print('Transcript saved')  # Success message print karo
        return True
    elif error:  # Agar error mila
        print("Error!!!", error)  # Error message print karo
        return False