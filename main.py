            import pyaudio
            import os 
            import pandas as  pd 
            from pydub import AudioSegment
            from gtts import gTTS
            def textToSpeech(text,filename):
                pass
            def mergeAudios(audios):
                pass
            def genrateSkeleton():
                audio=AudioSegment.from_mp3('audio.mp3')
                start=48600
                finish=51920
                audioProcessed=audio[start:finish]
                audioProcessed.export("1_hindi.mp3",format="mp3")
            def genrateAnnouncement(filename):
                pass
            if __name__ == "__main__":
                print("Genrating Skeleton")
                genrateSkeleton()
                print("now genrating skeleton")
                genrateAnnouncement("Book1.xlsx")
                