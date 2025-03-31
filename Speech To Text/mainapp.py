import requests  # HTTP requests bhejne ke liye library import ki.
import time  # Delay ya sleep ke liye time module import kiya.
from api_secrets import API_KEY_ASSEMBLYAI  # API key ko alag file se import kiya.

upload_endpoint = 'https://api.assemblyai.com/v2/upload'  # Audio file upload karne ka endpoint.
transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'  # Transcription ke liye endpoint.

headers_auth_only = {'authorization': API_KEY_ASSEMBLYAI}  # Sirf authorization ke liye headers.

headers = {  # Authorization aur content type ke liye headers.
    "authorization": API_KEY_ASSEMBLYAI,
    "content-type": "application/json"
}

CHUNK_SIZE = 5_242_880  # File ko 5MB ke chunks mein read karne ke liye size define kiya.

#upload
def upload(filename):  # File ko upload karne ka function.
    def read_file(filename):  # File ko chunks mein read karne ka nested function.
        with open(filename, 'rb') as f:  # File ko binary mode mein open kiya.
            while True:  # Infinite loop jab tak file ka data khatam na ho.
                data = f.read(CHUNK_SIZE)  # Chunk size ke hisaab se data read kiya.
                if not data:  # Agar data khatam ho gaya to loop break.
                    break
                yield data  # Chunk ko return kiya.

    print("Uploading file...")
    upload_response = requests.post(upload_endpoint, headers=headers_auth_only, data=read_file(filename))  
    if upload_response.status_code != 200:  # Error handling added.
        print("Error during upload:", upload_response.json())
        return None
    print("Upload response:", upload_response.json())  # Debug print
    return upload_response.json().get('upload_url')  # Upload URL return kiya.

#transcribe
def transcribe(audio_url):  # Audio URL ko transcribe karne ka function.
    transcript_request = {  # Request body mein audio URL bheja.
        'audio_url': audio_url
    }

    print("Requesting transcription...")
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)  
    if transcript_response.status_code != 200:  # Error handling added.
        print("Error during transcription request:", transcript_response.json())
        return None
    print("Transcription response:", transcript_response.json())  # Debug print
    return transcript_response.json().get('id')  # Transcription ID return kiya.

#polling  
def poll(transcript_id):  # Transcription ka status check karne ka function.
    polling_endpoint = transcript_endpoint + '/' + transcript_id  # Polling endpoint banaya.
    polling_response = requests.get(polling_endpoint, headers=headers)  
    if polling_response.status_code != 200:  # Error handling added.
        print("Error during polling:", polling_response.json())
        return None
    print("Polling response:", polling_response.json())  # Debug print
    return polling_response.json()  # Response JSON return kiya.

def get_transcription_result_url(url):  # Transcription ka result lene ka function.
    transcribe_id = transcribe(url)  # Transcription ID liya.
    if not transcribe_id:  # Error handling added.
        print("Failed to get transcription ID.")
        return None, "Transcription ID not generated."

    while True:  # Infinite loop jab tak transcription complete na ho.
        data = poll(transcribe_id)  # Polling function call kiya.
        if not data:  # Error handling added.
            return None, "Polling failed."

        if data['status'] == 'completed':  # Agar status completed hai to result return karo.
            return data, None
        elif data['status'] == 'error':  # Agar error hai to error return karo.
            return data, data['error']
            
        print("waiting for 30 seconds")  # Status check karne ke liye wait message print kiya.
        time.sleep(30)  # 30 seconds ka delay.

#save transcript    
def save_transcript(url, title):  # Transcript ko save karne ka function.
    data, error = get_transcription_result_url(url)  # Transcription result aur error liya.
    
    if data:  # Agar data available hai.
        filename = title + '.txt'  # File ka naam banaya.
        with open(filename, 'w') as f:  # File ko write mode mein open kiya.
            f.write(data['text'])  # Transcription text ko file mein likha.
        print('Transcript saved')  # Success message print kiya.
    elif error:  # Agar error hai.
        print("Error!!!", error)  # Error message print kiya.

# Summary of the program flow:
# 1. Upload Function:
#    - Audio file ko chunks mein read karta hai (5MB ke parts).
#    - File ko AssemblyAI ke upload endpoint par bhejta hai.
#    - Upload hone ke baad server se `upload_url` return karta hai.
#
# 2. Transcribe Function:
#    - Upload ki gayi audio file ka URL (upload_url) ko AssemblyAI ke transcription endpoint par bhejta hai.
#    - Server se ek unique transcription ID (`id`) return hota hai.
#
# 3. Poll Function:
#    - Transcription ID ke basis par transcription ka status check karta hai.
#    - Status `completed` hone par transcription ka result return karta hai.
#    - Agar koi error hoti hai, toh error message return karta hai.
#
# 4. Get Transcription Result URL Function:
#    - Transcription ID ko repeatedly poll karta hai jab tak transcription complete ya error na ho.
#    - Agar transcription complete hoti hai, toh transcription ka data return karta hai.
#    - Agar error hoti hai, toh error message return karta hai.
#
# 5. Save Transcript Function:
#    - Transcription ka result aur error ko handle karta hai.
#    - Agar transcription successful hoti hai, toh result ko ek text file mein save karta hai.
#    - Agar error hoti hai, toh error message print karta hai.


