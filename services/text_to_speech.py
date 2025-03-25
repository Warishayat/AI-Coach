from bark import SAMPLE_RATE, generate_audio, preload_models  # Bark will work when model gives back response in the form of final_text
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
from huggingface_hub import login
import os



print("Load the Model")
#load the models
preload_models()

print("Model is successfully Loaded")

def generate_speech_from_text(final_response):
    """
    Converts the final_response text into speech using Bark and plays it.
    
    Args:
        final_response (str): The text that will be converted into speech.
    """
    # Generate audio from the provided text
    audio_array = generate_audio(final_response)

    # Save the generated audio to a WAV file
    write_wav("Bark-response.wav", SAMPLE_RATE, audio_array)

    # Play the generated audio
    return Audio(audio_array, rate=SAMPLE_RATE)

if __name__ == "__main__":
    final_response = "Hello, this is the response converted to speech."
    generate_speech_from_text(final_response)
