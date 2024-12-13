import time
from SpeechUtils import speak

class VoiceAssistant:
    def voiceAssistantInforamtion(self=0,name="Ева",LanguageOfSpeaking=["Русский","English"],LanguageOfRecognition=["Русский","Еnglish"]):
        toString = (f"Здравствуйте! Меня зовут {name} \n"
                    f"Постараюсь помочь Вам со всем о чем попросите!")
        print(toString)
        speak(toString)
# TODO -> озвучивает только toString, дальше ничего не говорит