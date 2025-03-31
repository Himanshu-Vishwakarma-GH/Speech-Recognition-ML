# Speech Recognition and Sentiment Analysis

This project performs speech recognition on YouTube videos and analyzes the sentiments of the transcribed text. It uses the following technologies:

- **AssemblyAI API**: For speech-to-text transcription and sentiment analysis.
- **YouTube-DL**: To extract video and audio information from YouTube.
- **Python**: For scripting and automation.

## Features

1. Extract audio from YouTube videos.
2. Perform speech-to-text transcription.
3. Analyze sentiments (Positive, Negative, Neutral) in the transcribed text.
4. Save results in text and JSON formats.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Speech-Recognition-Python
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your AssemblyAI API key in `api_secrets.py`:
   ```python
   API_KEY_ASSEMBLYAI = 'your_api_key_here'
   ```

4. Run the script:
   ```bash
   python main.py
   ```

## File Structure

- `main.py`: Main script to run the program.
- `api.py`: Handles API requests to AssemblyAI.
- `yt_extractor.py`: Extracts video and audio information from YouTube.
- `api_secrets.py`: Stores the AssemblyAI API key.
- `data/`: Folder to store transcripts and sentiment analysis results.

## Sample Output

- **Text File**: Contains the transcribed text.
- **JSON File**: Contains sentiment analysis results.

## Notes

- Ensure the `data` folder exists or is created automatically by the script.
- Replace the sample YouTube URL in `main.py` with your desired video URL.

## License

This project is licensed under the MIT License.
