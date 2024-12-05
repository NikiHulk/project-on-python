import speech_recognition
import os

import CheckWeather
import Greetings
import Farewell
import Apologies


#def apologies(*args: tuple):
#    if not args[0]: return Apologies.Apologies.playApologies(self=0)


def farewellAndQuit(*args: tuple):
    if not args[0]: return Farewell.Farewell.farewellAndQuit(self=0)


def greetings(*args: tuple):
    if not args[0]: return Greetings.Greetings.playGreetings(self=0)


def checkWeather(*args: tuple):
    if not args[0]: return CheckWeather.checkWeatherNow("Moscow")


def recordAndRecognizeAudio(*args: tuple):
    with microphone:

        recognizedData = ""

        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Слушаю...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("Вас не слышно! Пожалуйста, проверьте свой микрофон.")
            return
        try:
            print("Распознаю...")
            recognizedData = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        return recognizedData


commands = {
    ("здравствуйте", "здравствуй", "здарова", "привет"): greetings,
    #("ты меня утомила", "я устал от тебя", "ты тупая", "тебе надо развиваться"): apologies,
    ("до свидания", "goodbye", "я ухожу", "прощай", "пока"): farewellAndQuit,
    # ("search", "google", "find", "найди"): search_for_term_on_google,
    # ("video", "youtube", "watch", "видео"): search_for_video_on_youtube,
    # ("wikipedia", "definition", "about", "определение", "википедия"): search_for_definition_on_wikipedia,
    # ("translate", "interpretation", "translation", "перевод", "перевести", "переведи"): get_translation,
    # ("language", "язык"): change_language,
    ("какая погода сегодня", "какая сегодня погода", "погода", "прогноз"): checkWeather,
    #("подбрось монету", "орёл или решка?", "кинь жребий"): toss_coin,
    # ("facebook", "person", "run", "пробей", "контакт"): run_person_through_social_nets_databases,
    # ("toss", "coin", "монета", "подбрось"): toss_coin,
}


def executeCommandWithName(command_name: str, *args: list):
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass

import random
import pyttsx3

def toss_coin():
    """Симулирует подбрасывание монетки и возвращает результат."""
    return random.choice([[["орел"], ["решка"]], [["tails"], ["heads"]]])

def speak_result(result, language='ru'):
    """Воспроизводит результат подбрасывания монетки."""
    try:
        engine = pyttsx3.init()
        # if language == 'ru':
        #     engine.say("Подбрось монету")
        # else:
        #     engine.say("Flip a coin")
        if language == 'en':
            engine.say(f"It's {result}!")
        else:
            engine.say(f"Выпало {result}!")
        engine.runAndWait()
    except pyttsx3.engine.EngineError as e:
        print(f"Ошибка при воспроизведении речи: {e}")
    except Exception as e:
        print(f"Произошла неизвестная ошибка: {e}")


if __name__ == "__main__":
    result = toss_coin()
    language = input("Выберите язык (ru/en): ").lower()
    if language not in ['ru', 'en']:
        print("Неверный язык. Используется русский по умолчанию.")
        language = 'ru'
    speak_result(result, language)

if __name__ == "__main__":

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        voiceInput = recordAndRecognizeAudio()
        os.remove("microphone-results.wav")

        print(voiceInput)

        voiceInput = voiceInput.split(" ")
        command = voiceInput[0]
        commandOptions = [str(inputPart) for inputPart in voiceInput[1:len(voiceInput)]]
        executeCommandWithName(command, commandOptions)

# TODO -> доделать остальные сервисы!
# TODO -> не считывает больше 1 слова. Надо решить
