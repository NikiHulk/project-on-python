import time
from SpeechUtils import speak

class VoiceAssistant:
    def typeAnimation(text, speed=0.02):
        for char in text:
            print(char, end='', flush=True)  # Печатаем символ, не добавляя новой строки
            time.sleep(speed)  # Задержка между символами
        print()  # Печатаем новую строку после завершения анимации

    def voiceAssistantInforamtion(self=0,name="Ева",LanguageOfSpeaking=["Русский","English"],LanguageOfRecognition=["Русский","Еnglish"]):
        toString = (f"Здравствуйте! Меня зовут {name} \n"
                    f"Постараюсь помочь Вам со всем о чем попросите! \n"
                    f"Языки на которых я умею разговаривать: {LanguageOfSpeaking[0]} и {LanguageOfSpeaking[1]} \n"
                    f"Языки на которых я могу понять Вас: {LanguageOfRecognition[0]} и {LanguageOfRecognition[1]}")
        print(toString)
        speak(toString)
    typeAnimation(voiceAssistantInforamtion())
# TODO -> озвучивает только toString, дальше ничего не говорит