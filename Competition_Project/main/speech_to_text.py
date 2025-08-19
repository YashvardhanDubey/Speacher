import os
import speech_recognition as sr
import tempfile
import sounddevice as sd
import scipy.io.wavfile as wav

r = sr.Recognizer()

def record_speech():

    fs = 44100  # Sample rate
    temp_wav_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav', dir="audio_files")
    #file_path = os.path.join("audio_files", f"{uuid.uuid4().hex}.wav")
    file_path=temp_wav_file.name

    mydata = sd.rec(int(3*fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    wav.write(file_path, fs, mydata)
    try:
        with sr.AudioFile(file_path) as source:
            r.adjust_for_ambient_noise(source,duration=0.2)
            re_audio=r.record(source)
            text_given=r.recognize_google(re_audio)
            return text_given

    except sr.RequestError as re:
        print("Couldn't request results", re)
    except sr.UnknownValueError:
        print("Unknown Error Occurred")

def output_speech(text):
    with open("Output.txt","a+") as f:
        f.write("spoken text:"+text)
        f.write("\n")
    return