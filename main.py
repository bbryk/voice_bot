import speech_recognition as sr
from  selenium import webdriver
from speak import speak
from audio import record
from music import play_music
import alsaaudio

FILENAME = "audio_files/output.wav"
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
            if text.strip() == "play music":
                speak("Which song you want to play?")
                record(seconds=5)
                try:
                    text = recognize_audio_file()
                    speak(f'Finished recording. Playing {text}')
                    play_music(text)

                except sr.UnknownValueError:
                    speak('I didn\'t recognise the text. Say play music if you want to play music')



            if text.strip() =='stop':
                speak("I'm outta here")
                break

            if ''.join(text.strip().split()[:2])=='setvolume':
                m = alsaaudio.Mixer()
                current_volume = m.getvolume()
                m.setvolume(int(text.strip().split()[-1]))




        except sr.UnknownValueError:
            continue





if __name__=='__main__':


    main()





































# def api_create():
#     from googleapiclient.discovery import build
#     api_key = key
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     return youtube


# if __name__=="__main__":
#     youtube = api_create()
#     request = youtube.videos().list(
#         forUsername='EugeneSagaz'
#     )
#     response = request.execute()
#     pprint(response)
