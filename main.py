import speech_recognition as sr
from speak import speak

from audio import record
FILENAME = "output1.wav"
def recognize_audio_file():
    r = sr.Recognizer()
    with sr.AudioFile(FILENAME) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        return text

def main():
    while True:
        record()
        try:
            text = recognize_audio_file()
            print(text)
            if text.strip() == "play":
                print('yes')
            if text.strip() =='stop':
                break
        except sr.UnknownValueError:
            continue













































# def api_create():
#     from googleapiclient.discovery import build
#     api_key = 'AIzaSyA9Jq41IossqPkJwZq8p6jJaj6L_ZfN25U'
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     return youtube


# if __name__=="__main__":
#     youtube = api_create()
#     request = youtube.videos().list(
#         forUsername='EugeneSagaz'
#     )
#     response = request.execute()
#     pprint(response)








