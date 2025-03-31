# Speech Recognition - Python

This project demonstrates a Python-based speech-to-text application using the AssemblyAI API. It allows users to upload audio files, transcribe them into text, and save the transcription to a file.

## Features

- **Audio Upload**: Upload audio files in chunks to the AssemblyAI API.
- **Transcription**: Convert audio files to text using AssemblyAI's transcription service.
- **Polling**: Check the status of the transcription process until completion.
- **Save Transcription**: Save the transcription result to a `.txt` file.

## Requirements

- Python 3.7 or higher
- An AssemblyAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/speech-recognition-python.git
   cd speech-recognition-python/Speech\ To\ Text
   ```

2. Install the required Python libraries:
   ```bash
   pip install requests
   ```

3. Add your AssemblyAI API key in the `api_secrets.py` file:
   ```python
   API_KEY_ASSEMBLYAI = "your_api_key_here"
   ```

## Usage

1. Place your audio file in the project directory.

2. Run the `mainapp.py` script:
   ```bash
   python mainapp.py
   ```

3. Use the provided functions to:
   - Upload the audio file.
   - Transcribe the audio.
   - Save the transcription to a text file.

## File Structure

- `mainapp.py`: Contains the main logic for uploading, transcribing, polling, and saving transcriptions.
- `api_secrets.py`: Stores the AssemblyAI API key.
- `README.md`: Documentation for the project.

## Example Workflow

1. **Upload Audio**:
   ```python
   upload_url = upload("audio_file.mp3")
   ```

2. **Transcribe Audio**:
   ```python
   transcription_id = transcribe(upload_url)
   ```

3. **Poll for Status**:
   ```python
   result = poll(transcription_id)
   ```

4. **Save Transcription**:
   ```python
   save_transcript(upload_url, "transcription_title")
   ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

- [AssemblyAI](https://www.assemblyai.com/) for their transcription API.
