import os
from dotenv import load_dotenv
import whisper

load_dotenv()

Hugging_face_token = os.getenv("HF_API_TOKEN")
if Hugging_face_token:
    os.environ["HF_API_TOKEN"] = Hugging_face_token
else:
    raise ValueError("Hugging Face API token is missing.")


model = whisper.load_model("medium")

def transcribe_voice(audio_path):
    """
    Transcribes the given audio file to text using the Whisper model.
    
    :param audio_path: Path to the audio file to transcribe
    :return: Transcription result as a string or None if failed
    """
    try:
        if audio_path:
            stt_response = model.transcribe(audio_path)
            return stt_response["text"]
        else:
            print("No audio path provided.")
            return None
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # audio_path = "path_to_audio_file.wav"  
    # response = transcribe_voice(audio_path)
    # if response:
    #     print("Transcribed text:", response)
    # else:
    #     print("Failed to transcribe the audio.")
    print("All set till here")
