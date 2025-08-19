### **Speech Impediment Helper:**



An interactive Python application designed to assist individuals in practicing speech.

It provides Text-to-Speech (TTS) and Speech-to-Text (STT) functionalities along with an accuracy checker to help users improve pronunciation and fluency.



#### **Features:**



##### Text-to-Speech (TTS):



Type text and hear it spoken aloud.

Switch between male/female voices (system dependent)(Currently does not work on Linux, haven't tried on macos).

Custom Phrase Buttons. (Note: They dont save when you quit the program. Can be fixed by loading a simple file.)

Some common phrases(e.g., Hello, Thank you).



##### Speech-to-Text (STT):



Speak into your microphone and see the recognized text.

Uses Google’s Speech Recognition API via speech\_recognition.

Accuracy Checker.

Input a phrase, then attempt to say it.

The system compares your spoken version with the target using Levenshtein distance.

Displays accuracy percentage and motivational feedback.



##### General:

Built with Tkinter.

Tabs for TTS and STT functionality.

Background images and emoji for a friendly feel.



#### Tech Stack:

Python 3.11+



#### Libraries Used:

tkinter (GUI)

pyttsx3 (TTS)

SpeechRecognition (STT)

sounddevice + scipy (audio recording)

python-Levenshtein (accuracy checking)

emoji (UI labels)

📂 Project Structure

