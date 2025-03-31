import json  # JSON files ko handle karne ke liye import
import os  # File aur folder operations ke liye import
from yt_extractor import get_video_info, get_audio_url  # YouTube se video info aur audio URL extract karne ke liye
from api import save_transcript  # Transcript save karne ke liye function import

# Function jo video ke sentiments ko save karega
def save_video_sentiments(url):
    video_info = get_video_info(url)  # YouTube video ki information extract karo
    url = get_audio_url(video_info)  # Audio URL extract karo
    if url:  # Agar audio URL mil gaya
        title = video_info['title']  # Video ka title le lo
        title = title.strip().replace(" ", "_")  # Title ko clean aur format karo
        title = "data/" + title  # Title ko data folder ke andar save karne ke liye path banao
        save_transcript(url, title, sentiment_analysis=True)  # Transcript save karo aur sentiment analysis enable karo

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)  # Data folder ko ensure karo ki exist kare, agar nahi hai to create karo
    
    # save_video_sentiments("https://youtu.be/e-kSGNzu0hM")  # Example URL ko uncomment karke test kar sakte ho
    
    file_path = "data/iPhone_13_Review:_Pros_and_Cons_sentiments.json"  # JSON file ka path define karo
    if not os.path.exists(file_path):  # Agar file exist nahi karti
        print(f"File '{file_path}' does not exist. Creating a sample JSON file...")  # Error message print karo
        sample_data = [  # Sample data create karo
            {"text": "Great product!", "sentiment": "POSITIVE"},
            {"text": "Not worth the price.", "sentiment": "NEGATIVE"},
            {"text": "It's okay, nothing special.", "sentiment": "NEUTRAL"}
        ]
        with open(file_path, "w") as f:  # File ko write mode me open karo
            json.dump(sample_data, f, indent=4)  # Sample data ko JSON file me save karo
        print(f"Sample JSON file created at '{file_path}'.")  # Confirmation message print karo
    else:
        with open(file_path, "r") as f:  # File ko read mode me open karo
            data = json.load(f)  # JSON data ko load karo
        
        positives = []  # Positive sentiments ke liye list
        negatives = []  # Negative sentiments ke liye list
        neutrals = []  # Neutral sentiments ke liye list
        for result in data:  # Har result ke liye loop
            text = result["text"]  # Text extract karo
            if result["sentiment"] == "POSITIVE":  # Agar sentiment positive hai
                positives.append(text)  # Positive list me add karo
            elif result["sentiment"] == "NEGATIVE":  # Agar sentiment negative hai
                negatives.append(text)  # Negative list me add karo
            else:  # Agar sentiment neutral hai
                neutrals.append(text)  # Neutral list me add karo
            
        n_pos = len(positives)  # Positive sentiments ki count
        n_neg = len(negatives)  # Negative sentiments ki count
        n_neut = len(neutrals)  # Neutral sentiments ki count

        print("Num positives:", n_pos)  # Positive count print karo
        print("Num negatives:", n_neg)  # Negative count print karo
        print("Num neutrals:", n_neut)  # Neutral count print karo

        if n_pos + n_neg > 0:  # Agar positive aur negative ka sum zero se bada hai
            r = n_pos / (n_pos + n_neg)  # Positive ratio calculate karo
            print(f"Positive ratio: {r:.3f}")  # Positive ratio print karo
        else:
            print("No positive or negative sentiments found. Positive ratio cannot be calculated.")  # Error message
