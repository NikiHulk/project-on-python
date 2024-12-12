import speech_recognition as sr
import os
import ClassVolumeManager as vm
import Exchange
import NoteManagerClass
import Greetings  # Импортируем модуль с классом Greetings
import Farewell   # Импортируем модуль с классом Farewell
import CheckWeather # Импортируем модуль с классом CheckWeather (или функцией)
import Apologies  # Импортируем модуль с классом Apologies (или функцией)
import Translating
import VoiceAssistantClass
from SpeechUtils import speak
from TossCoin import TossCoin


def recordAndRecognizeAudio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        try:
            print("Слушаю...")
            speak("Слушаю...")
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=8)
            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())
            print("Распознаю...")
            speak("Распознаю")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()
            return recognized_data
        except sr.WaitTimeoutError:
            print("Вас не слышно! Пожалуйста, проверьте свой микрофон.")
            speak("Вас не слышно! Пожалуйста, проверьте свой микрофон.")
            return None
        except sr.UnknownValueError:
            print("Не удалось распознать речь.")
            speak("Не удалось распознать речь.")
            return None
        except Exception as e:
            print(f"Ошибка при распознавании: {e}")
            speak(f"Ошибка при распознавании: {e}")
            return None


commands = {
    ("здравствуйте", "здравствуй", "здарова", "привет", ): lambda: Greetings.Greetings().playGreetings(),  # Обратите внимание на лямбда-функцию
    ("до свидания", "goodbye", "я ухожу", "прощай", "пока", ): lambda: Farewell.Farewell().farewellAndQuit(), # лямбда-функция
    ("какая погода сегодня", "какая сегодня погода", "погода", "какая погода в городе"): lambda: CheckWeather.checkWeatherNow("Moscow"), # лямбда-функция
    ("создать заметку", "записать", "новая заметка"): lambda: create_note_interaction(),
    ("прочитать заметки", "заметки", "посмотреть заметки"): lambda: NoteManagerClass.NotesManager().ReadNotes(),
    ("удалить заметку", "удалить запись"): lambda: delete_note_interaction(),
    ("курс","какой курс", "курс валют"): lambda: Exchange.exchangeRate(currencyUnit=str(input('Введите валюту: '))),
    ("подбрось монетку", "кинь монету", "сыграем в лотерею?"): lambda: TossCoin.tossCoin(self=0),
    ("переводчик", "перевод"): lambda: Translating.translate(),
    ("громче", "увеличить громкость"): lambda: vm.VolumeManager().AdjustVolume(10),
    ("тише", "уменьшить громкость"): lambda: vm.VolumeManager().AdjustVolume(-10),
    ("отключить звук", "без звука"): lambda: vm.VolumeManager().mute(),
    ("включить звук",): lambda: vm.VolumeManager().mute(),
    # ... добавьте другие команды ...
}


def create_note_interaction():
    """Взаимодействие с пользователем для создания заметки."""
    try:
        speak("Введите текст заметки")
        note_text = input("Введите текст заметки: ")
        NoteManagerClass.NotesManager().CreateNote(note_text)
        print("Заметка создана.")
        speak("Заметка создана.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        speak(f"Произошла ошибка: {e}")
def delete_note_interaction():
    """Взаимодействие с пользователем для удаления заметки."""
    try:
        NoteManagerClass.NotesManager().ReadNotes()  # Сначала показать список заметок
        if not NoteManagerClass.NotesManager().notes: # проверка на наличие заметок
            print("Нет заметок для удаления")
            speak("Нет заметок для удаления")
            return

        while True:
            try:
                speak("Введите номер заметки для удаления (или 0 для отмены)")
                note_index = int(input("Введите номер заметки для удаления (или 0 для отмены): "))
                if note_index == 0:
                    return  # Отмена удаления
                NoteManagerClass.NotesManager().DeleteNote(note_index)
                print("Заметка удалена.")
                speak("Заметка удалена.")
                break  # Выход из цикла после успешного удаления
            except ValueError:
                print("Неверный формат ввода. Пожалуйста, введите число.")
                speak("Неверный формат ввода. Пожалуйста, введите число.")
            except IndexError:
                print("Заметки с таким номером не существует.")
                speak("Заметки с таким номером не существует.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        speak(f"Произошла ошибка: {e}")


def executeCommand(command_phrase: str):
    for key, func in commands.items():
        for keyword in key:
            if keyword in command_phrase:
                try:
                    func()
                except Exception as e:
                    print(f"Ошибка при выполнении команды: {e}")
                    speak(f"Ошибка при выполнении команды: {e}")
                return
    print("Неизвестная команда.")
    speak("Неизвестная команда.")


if __name__ == "__main__":
    assistant = VoiceAssistantClass.VoiceAssistant# Создаем экземпляр класса VoiceAssistant
      # Вызываем метод для объявления информации о помощнике
    while True:
        voice_input = recordAndRecognizeAudio()
        if voice_input:
            os.remove("microphone-results.wav")
            print(f"Распознано: {voice_input}")
            executeCommand(voice_input)
    assistant.announce_information()