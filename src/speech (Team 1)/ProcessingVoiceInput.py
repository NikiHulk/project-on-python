import speech_recognition as sr
import os
import NoteManagerClass
import Greetings  # Импортируем модуль с классом Greetings
import Farewell   # Импортируем модуль с классом Farewell
import CheckWeather # Импортируем модуль с классом CheckWeather (или функцией)
import Apologies  # Импортируем модуль с классом Apologies (или функцией)
import TossCoin
import pyttsx3

engine = pyttsx3.init()
def speak(text):
    """Функция для озвучивания текста."""
    engine.say(text)
    engine.runAndWait()
def recordAndRecognizeAudio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        try:
            print("Слушаю...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())
            print("Распознаю...")
            speak("Распознаю...")
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
    ("здравствуйте", "здравствуй", "здарова", "привет", "Салам", "Приветствую", "Hi", "Hello"): lambda: Greetings.Greetings().playGreetings(),  # Обратите внимание на лямбда-функцию
    ("до свидания", "goodbye", "я ухожу", "прощай", "пока", "bye-bye", "До встречи"): lambda: Farewell.Farewell().farewellAndQuit(), # лямбда-функция
    ("какая погода сегодня", "какая сегодня погода", "погода", "прогноз", "прогноз погоды", "что там по погоде"): lambda: CheckWeather.checkWeatherNow("Moscow"), # лямбда-функция
    ("создать заметку", "записать", "новая заметка", "напиши заметку"): lambda: create_note_interaction(),
    ("прочитать заметки", "заметки", "чтение заметок"): lambda: NoteManagerClass.NotesManager().ReadNotes(),
    ("удалить заметку", "удалить запись", "сотри заметку"): lambda: delete_note_interaction(),
    ("кинь монету", "кинь жребий", "подбрось монету"): lambda: TossCoin.TossCoin.tossCoin()
    # ... добавьте другие команды ...
}
def create_note_interaction():
    """Взаимодействие с пользователем для создания заметки.
    с помошью голоса """
    try:
        note_text = input("Введите текст заметки: ")
        NoteManagerClass.NotesManager().CreateNote(note_text)
        print("Заметка создана.")
        speak("Заметка создана")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        speak(f"Произошла ошибка: {e}")
def delete_note_interaction():
    """Взаимодействие с пользователем для удаления заметки.
    с помощью голоса"""
    try:
        NoteManagerClass.NotesManager().ReadNotes()  # Сначала показать список заметок
        if not NoteManagerClass.NotesManager().notes: # проверка на наличие заметок
            print("Заметок нет для удаления")
            speak("Заметок нет для удаления")
            return

        while True:
            try:
                note_index = int(input("Введите номер заметки для удаления (или 0 для отмены): "))
                if note_index == 0:
                    return  # Отмена удаления
                NoteManagerClass.NotesManager().DeleteNote(note_index)
                print("Заметка удалена.")
                speak("Заметка удалена")
                break  # Выход из цикла после успешного удаления
            except ValueError:
                print("Неверный формат ввода. Пожалуйста, введите число.")
                speak("Неверный формат ввода. Пожалуйста, введите число")
            except IndexError:
                print("Заметки с таким номером не существует.")
                speak("Заметки с таким номером не существует")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        speak(f"Произошла ошибка: {e}")


def executeCommand(command_phrase: str):
    for key, func in commands.items():
        for keyword in key:
            if keyword in command_phrase:
                try:
                    response = func()
                    if response:
                        speak(str(response))
                    else:
                        speak("Команда выполнена")
                except Exception as e:
                    print(f"Ошибка при выполнении команды: {e}")
                    speak(f"Ошибка при выполнении команды: {e}")
                return
    print("Неизвестная команда.")
    speak("Неизвестная команда.")

if __name__ == "__main__":
    speak("Здравствуйте! Чем я могу вам помочь?")
    while True:
        voice_input = recordAndRecognizeAudio()
        if voice_input:
            os.remove("microphone-results.wav")
            print(f"Распознано: {voice_input}")
            executeCommand(voice_input)