import speech_recognition as sr


def audio_to_text(audio_file):
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)

    try:
        # Use Google Web Speech API for speech recognition
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Error: {e}" 
    

audio_file_path='/Users/siddhijain/Desktop/MoMi/DIALOGUE.wav'
result = audio_to_text(audio_file_path)