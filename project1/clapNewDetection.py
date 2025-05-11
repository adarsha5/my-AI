# import librosa
# import numpy as np

# # Load the audio file
# audio_file = 'file.wav'
# y, sr = librosa.load(audio_file, sr=None)

# # Define the threshold for clap detection
# threshold = 0.5

# # Calculate the onset strength envelope
# onset_env = librosa.onset.onset_strength(y, sr=sr)

# # Normalize the onset strength envelope
# onset_env_norm = (onset_env - np.mean(onset_env)) / np.std(onset_env)

# # Detect clap based on the threshold
# clap_indices = np.where(onset_env_norm > threshold)[0]

# # Print the detected clap indices
# print("Clap detected at indices:", clap_indices)


import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
def clapNewDetection():
    # Define the parameters
    duration = 5  # Duration of the recording in seconds
    fs = 44100  # Sample rate
    threshold = 0.02  # Threshold for clap detection

    # Record audio
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Recording finished.")

    # Convert recording to mono and normalize
    audio = np.mean(recording, axis=1)
    audio /= np.max(np.abs(audio))

    # Detect claps
    clap_indices = np.where(audio > threshold)[0]

    # Print the detected clap indices
    print("Clap detected at indices:", clap_indices)

    if clap_indices[0] != 0 :
        print("Yes You Clapped")
        return True
    else:
        print("No You Clapped")

clapNewDetection()

