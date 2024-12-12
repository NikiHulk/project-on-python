import speech_recognition as SpeechRecognizer
import os
import time
import threading

from sympy.polys.polyconfig import query

import CheckWiki
import ClassVolumeManager as VolumeManager
import Exchange
import NoteManagerClass
import Greetings
import Farewell
import CheckWeather
import Apologies
import Translating
import VoiceAssistantClass
from SpeechUtils import speak
from TossCoin import TossCoin
from GetMoscowNews import GetMoscowNewsFromRss
from Reminder import reminder
from Reminder import setReminder
import schedule
import PageOpener
import CheckMaps
import webbrowser

from VoiceAssistantClass import VoiceAssistant


def listenForWakeWord():
    """Функция для прослушивания ключевого слова для активации ассистента."""
    recognizer = SpeechRecognizer.Recognizer()
    with SpeechRecognizer.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        while True:
            try:
                print("Слушаю ключевое слово...")
                audio = recognizer.listen(source, timeout=8, phrase_time_limit=8)
                command = recognizer.recognize_google(audio, language="ru").lower()
                print(f"Распознано: {command}")
                if "привет ева" in command:
                    print("Активировано! Команды можно говорить.")
                    speak(VoiceAssistant.voiceAssistantInforamtion())
                    listenForCommands()  # Активируем слушание команд после активации
            except SpeechRecognizer.UnknownValueError:
                continue
            except SpeechRecognizer.WaitTimeoutError:
                continue
            except Exception as e:
                print(f"Ошибка: {e}")


def listenForCommands():
    """Функция для прослушивания команд пользователя после активации ассистента."""
    recognizer = SpeechRecognizer.Recognizer()
    with SpeechRecognizer.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        while True:
            try:
                print("Слушаю команду...")
                speak("Слушаю команду...")
                audio = recognizer.listen(source, timeout=8, phrase_time_limit=8)
                commandPhrase = recognizer.recognize_google(audio, language="ru").lower()
                print(f"Распознано: {commandPhrase}")
                executeCommand(commandPhrase)  # Выполняем команду
            except SpeechRecognizer.UnknownValueError:
                print("Не удалось распознать команду.")
                speak("Не удалось распознать команду.")
            except SpeechRecognizer.WaitTimeoutError:
                print("Время ожидания истекло.")
                speak("Время ожидания истекло.")
            except Exception as e:
                print(f"Ошибка при распознавании: {e}")
                speak(f"Ошибка при распознавании: {e}")


def searchInYandex(query):
    """Функция для поиска в Yandex при неизвестной команде."""
    speak(f"Неизвестная команда: {query}. Хотите, чтобы я нашел это в Яндекс?")
    response = input(f"Неизвестная команда: {query}. Хотите, чтобы я нашел это в Яндекс? (да/нет): ").strip().lower()
    if response == "да" or response == "yes":
        searchUrl = f"https://yandex.ru/search/?text={query}"
        webbrowser.open(searchUrl)
        speak(f"Открываю результаты поиска в Яндекс для {query}.")
    else:
        speak("Хорошо, не буду искать.")


def executeCommand(commandPhrase: str):
    for key, func in commands.items():
        for keyword in key:
            if keyword in commandPhrase:
                try:
                    func()
                    return
                except Exception as e:
                    print(f"Ошибка при выполнении команды: {e}")
                    speak(f"Ошибка при выполнении команды: {e}")
                    return
    # Если команда не распознана, предложим поиск в Yandex
    print("Неизвестная команда. Попробуйте снова.")
    speak("Неизвестная команда. Попробуйте снова.")
    searchInYandex(commandPhrase)  # Добавляем поиск в Yandex для неизвестной команды


# Инициализация команд
commands = {
    ("здравствуйте", "здравствуй", "здарова", "привет",): lambda: Greetings.Greetings().playGreetings(),
    ("до свидания", "goodbye", "я ухожу", "прощай", "пока",): lambda: Farewell.Farewell().farewellAndQuit(),
    ("какая погода сегодня", "какая сегодня погода", "погода","какая погода в городе"): lambda: CheckWeather.checkWeatherNow(city=str(input("Введите город: "))),
    ("создать заметку", "записать", "новая заметка"): lambda: createNoteInteraction(),
    ("прочитать заметки", "заметки", "посмотреть заметки"): lambda: NoteManagerClass.NotesManager().readNotes(),
    ("удалить заметку", "удалить запись"): lambda: deleteNoteInteraction(),
    ("курс", "какой курс", "курс валют"): lambda: Exchange.exchangeRate(currencyUnit=str(input('Введите валюту: '))),
    ("подбрось монетку", "кинь монету", "сыграем в лотерею?"): lambda: connectTossCoin(),
    ("переводчик", "перевод"): lambda: Translating.translate(),
    ("громче", "увеличить громкость"): lambda: VolumeManager.VolumeManager().adjustVolume(10),
    ("тише", "уменьшить громкость"): lambda: VolumeManager.VolumeManager().adjustVolume(-10),
    ("отключить звук", "без звука"): lambda: VolumeManager.VolumeManager().mute(),
    ("включить звук",): lambda: VolumeManager.VolumeManager().mute(),
    ("новости", "новости дня", "что нового"): lambda: connectGetMoscowNews(),
    ("напоминание", "создай напоминание", "сделай напоминание"): lambda: connectReminder(),
    ("открой вконтакте", "вконтакте", "открой вк"): lambda: PageOpener.openVkontakte(),
    ("открой вк видео", "вконтакте видео", "видео вк", "вк видео"): lambda: PageOpener.openVkVideo(),
    ("открой кинопоиск", "кинопоиск"): lambda: PageOpener.openKinopoisk(),
    ("открой иви", "иви"): lambda: PageOpener.openIvi(),
    ("открой рутуб", "рутуб"): lambda: PageOpener.openRutube(),
    ("открой ютуб", "ютуб"): lambda: PageOpener.openYouTube(),
    ("открой telegram", "telegram"): lambda: PageOpener.openTelegram(),
    ("открой яндекс карты", "яндекс карты", "карты"): lambda: PageOpener.openYandexMaps(),
    ("дорога", "путь"): lambda: connectCheckMaps(),
    ("википедия","найди в википедии"): lambda: connectCheckWiki()
}

def connectCheckWiki():
    query = str(input("Введите ваш запрос: "))
    CheckWiki.searchInWikipedia(query)

def connectTossCoin():
    toss = TossCoin()
    speak("Введите количество подбрасываний монеты")
    numTosses = int(input("Введите количество подбрасываний монеты: "))  # Запрашиваем количество подбрасываний
    toss.tossCoin(numTosses)


def connectCheckMaps():
    startAddress = input("Введите адрес, откуда собираетесь добираться: ")
    endAddress = input("Введите адрес, куда собираетесь добираться: ")
    CheckMaps.getRouteBetweenAddresses(startAddress, endAddress)


def connectReminder():
    year = int(input("Введите год (YYYY): "))
    month = int(input("Введите месяц (MM): "))
    day = int(input("Введите день (DD): "))
    hour = int(input("Введите час (HH): "))
    minute = int(input("Введите минуту (MM): "))
    reminderText = input("Введите текст напоминания: ")

    setReminder(reminderText, year, month, day, hour, minute)

    while True:
        schedule.run_pending()
        time.sleep(1)  # Проверка каждые 1 секунду


def connectGetMoscowNews():
    num = input(
        "Введите номер интересующей вас новости, например 1, 2 ... 25: ")  # каждому номеру соответствует определенный топик из новостей
    rssUrl = f"https://govoritmoskva.ru/rss/news/{num}"
    moscowNews = GetMoscowNewsFromRss(rssUrl)
    if moscowNews:
        print("Новости Москвы:")
        for newsItem in moscowNews:
            print(f"- {newsItem}")
    return GetMoscowNewsFromRss(rssUrl)


def createNoteInteraction():
    """Взаимодействие с пользователем для создания заметки."""
    try:
        speak("Введите текст заметки")
        noteText = input("Введите текст заметки: ")
        NoteManagerClass.NotesManager().createNote(noteText)
        print("Заметка создана.")
        speak("Заметка создана.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        speak(f"Произошла ошибка: {e}")


def deleteNoteInteraction():
    """Взаимодействие с пользователем для удаления заметки."""
    try:
        NoteManagerClass.NotesManager().readNotes()  # Сначала показать список заметок
        if not NoteManagerClass.NotesManager().notes:  # проверка на наличие заметок
            print("Нет заметок для удаления")
            speak("Нет заметок для удаления")
            return

        while True:
            try:
                speak("Введите номер заметки для удаления (или 0 для отмены)")
                noteIndex = int(input("Введите номер заметки для удаления (или 0 для отмены): "))
                if noteIndex == 0:
                    return  # Отмена удаления
                NoteManagerClass.NotesManager().deleteNote(noteIndex)
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


if __name__ == "__main__":
    listenForWakeWord()# Запуск основного процесса
